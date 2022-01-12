# Input json file reading in programs format

import json as js

from model.impedances import Resistor
from model.impedances import Inductor
from model.impedances import Capacitor

from model.source import Voltage
from model.source import Current

from model.node import Node

Rth = 1.E-12

class Reader:

    # the json file must be valid, the validator does this process
    def __init__(self, json):
        # the parameter json is the json file path
        try:
            with open(json, 'r') as f:
                self.json = js.load(f)
        except Exception as error:
            print(error)
            self.json = {}
        self.data = {} # consolidated dictionary with converted objects

    def readNodes(self):
        # reads the components in node
        nodes = self.json['nodes']
        self.data['nodes'] = []
        for node in nodes:
            self.data['nodes'].append(Node.json(node, nodes[node]))
        print('Nodes processed: ')
        for node in self.data['nodes']:
            node.log()

    def readCircuits(self):
        # reads the components in circuits
        circuits = self.json['circuits']
        self.data['circuits'] = []
        for circuit in circuits:
            if 'resistance' in circuits[circuit]:
                self.data['circuits'].append(Resistor.json(circuit, circuits[circuit]))
            if 'inductance' in circuits[circuit]:
                self.data['circuits'].append(Inductor.json(circuit, circuits[circuit]))
            if 'capacitance' in circuits[circuit]:
                self.data['circuits'].append(Capacitor.json(circuit, circuits[circuit]))
        print('Circuits processed: ')
        for circuit in self.data['circuits']:
            circuit.log()

    def readSources(self):
        # reads the components in sources
        frequency = self.json['parameters']['frequency']
        sources = self.json['sources']
        self.data['sources'] = []
        for source in sources:
            if 'voltage' in sources[source]:
                self.data['sources'].append(Voltage.json(source, sources[source], frequency))
            if 'current' in sources[source]:
                self.data['sources'].append(Current.json(source, sources[source], frequency))
        print('Sources processed: ')
        for source in self.data['sources']:
            source.log()

    # preparing sources for simulation, converting all voltage sources into current sources
    def convertSources(self):
        for i in range(len(self.data['sources'])):
            source = self.data['sources'][i]
            if str(type(source).__name__) == 'Voltage':
                source = Current(source.name, source.id, source.f_id, source.t_id, source.voltage / Rth, source.angle, source.frequency)
                thevenin = Resistor('fictional thevenin', 'th <> ' + source.id, source.f_id, source.t_id, Rth)
                self.data['circuits'].append(thevenin)
                if source.f_id != '0':
                    for node in self.data['nodes']:
                        if node.id == source.f_id:
                            node.circuits.append(thevenin.id)
                if source.t_id != '0':
                    for node in self.data['nodes']:
                        if node.id == source.t_id:
                            node.circuits.append(thevenin.id)
            self.data['sources'][i] = source
            # print(source.current)
        print('Sources converted!')
        # print(self.data)

    # presenting systems consolidated data
    def log(self):
        print('\nSystem data: ')
        for node in self.data['nodes']:
            node.log()
        for circuit in self.data['circuits']:
            circuit.log()
        for source in self.data['sources']:
            source.log()
