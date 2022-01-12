# Input json file reading in programs format

import json as js

from model.impedances import Resistor
from model.impedances import Inductor
from model.impedances import Capacitor

from model.source import Voltage
from model.source import Current

from model.node import Node

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
