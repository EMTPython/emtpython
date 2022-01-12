# Input json file validation in programs format

import json as js

class Validation:

    def __init__(self, json):
        # the parameter json is the json file path
        try:
            with open(json, 'r') as f:
                self.json = js.load(f)
        except Exception as error:
            print(error)
            self.json = {}

    def validateName(self):
        # verify if the user remembered to define a name
        if 'name' not in self.json:
            return (False, 'The field name is missing in the input file...') # the name field does not exist
        return (True, 'Name field valid!')

    def validateParameters(self):
        # verify the simulation parameters
        if 'parameters' not in self.json or self.json['parameters'] == {}:
            return (False, 'The field parameters is missing in the input file...') # parameters list empty of inexistent
        p = self.json['parameters']
        if 'stop' not in p or 'dT' not in p or 'frequency' not in p:
            return (False, 'One of the necessary fields of parameters is missing...') # parameters fields missing
        if not isinstance(p['stop'], float) or not isinstance(p['dT'], float) or not isinstance(p['frequency'], float):
            return (False, 'The fields variable types (only Float is accepted) are wrong...') # parameters types wrong
        if p['stop'] < p['dT']:
            return (False, 'The stop time is minor than the timestep...') # total less than dT
        return (True, 'Parameters field is valid!')

    def validateNodes(self):
        # opens only the nodes key from the input file
        if 'nodes' not in self.json or self.json['nodes'] == {}:
            return (False, 'The field nodes is missing in the input file...') # nodes list empty or inexistent
        nodes = self.json['nodes']
        for node in nodes:
            if node == '0':
                return (False, 'There is no need to create the ground node...')
            if 'name' not in nodes[node] or 'circuits' not in nodes[node]:
                return (False, 'One of the necessary fields of node is missing for node -> ' + node) # nodes fields missing
            if not isinstance(nodes[node]['name'], str):
                return (False, 'Node name is not a string for node -> ' + node) # node name is not a string
            if nodes[node]['circuits'] == []:
                return (False, 'Node circuits is empty for node -> ' + node) # the is no circuit connected to the node
            for circuit in nodes[node]['circuits']:
                if not isinstance(circuit, str):
                    return (False, 'Node circuit identifier is not a string for node -> ' + node) # the circuit identifiers are not strings
        return (True, 'Nodes field is valid!')

    def validateCircuits(self):
        # opens only the circuits key from the input file
        if 'circuits' not in self.json or self.json['circuits'] == {}:
            return (False, 'The field circuits is missing in the input file...') # circuits list empty or missing
        circuits = self.json['circuits']
        for circuit in circuits:
            c = circuits[circuit]
            if 'name' not in c or 'f_id' not in c or 't_id' not in c:
                return (False, 'One of the necessary fields of circuit is missing for circuit -> ' + circuit) # circuits fields missing
            if 'resistance' not in c and 'inductance' not in c and 'capacitance' not in c:
                return (False, 'One of the necessary fields of circuit is missing for circuit -> ' + circuit) # circuits fields missing
            if not isinstance(c['name'], str) or not isinstance(c['f_id'], str) or not isinstance(c['t_id'], str):
                return (False, 'Circuit name, f_id or t_id is not a string for circuit -> ' + circuit) # fields are not strings
            if c['f_id'] == c['t_id']:
                return (False, 'Circuit f_id and t_id must be different for circuit -> ' +  circuit) # from and to are the same
            if 'resistance' in c and not isinstance(c['resistance'], float):
                return (False, 'Circuit resistance is not a float for circuit -> ' + circuit) # resistance is not float
            if 'inductance' in c and not isinstance(c['inductance'], float):
                return (False, 'Circuit inductance is not a float for circuit -> ' + circuit) # resistance is not float
            if 'capacitance' in c and not isinstance(c['capacitance'], float):
                return (False, 'Circuit capacitance is not a float for circuit -> ' + circuit) # resistance is not float
        return (True, 'Circuits field is valid!')

    def validateSources(self):
        # opens only the sources key from the input file
        if 'sources' not in self.json or self.json['sources'] == {}:
            return (False, 'The field sources is missing in the input file...') # sources list empty or missing
        sources = self.json['sources']
        for source in sources:
            c = sources[source]
            if 'name' not in c or 'f_id' not in c or 't_id' not in c or 'angle' not in c:
                return (False, 'One of the necessary fields of source is missing for source -> ' + source) # sources fields missing
            if 'voltage' not in c and 'current' not in c:
                return (False, 'One of the necessary fields of source is missing for source -> ' + source) # sources fields missing
            if not isinstance(c['name'], str) or not isinstance(c['f_id'], str) or not isinstance(c['t_id'], str) or not isinstance(c['angle'], float):
                return (False, 'Source name, f_id or t_id is not a string, or angle is not a float for source -> ' + source) # fields are not strings or floats
            if c['f_id'] == c['t_id']:
                return (False, 'Source f_id and t_id must be different for source -> ' +  source) # from and to are the same
            if 'voltage' in c and not isinstance(c['voltage'], float):
                return (False, 'Source voltage is not a float for source -> ' + source) # voltage is not float
            if 'current' in c and not isinstance(c['current'], float):
                return (False, 'Source current is not a float for source -> ' + source) # current is not float
        return (True, 'Sources field is valid!')

    def checkIds(self):
        # checks if identificators correspond
        # if nodes reference existing circuits
        # if circuits reference existing nodes
        nodes = self.json['nodes']
        circuits = self.json['circuits']
        sources = self.json['sources']
        # verifying if nodes reference existing circuits
        for node in nodes:
            n = nodes[node]
            c = n['circuits']
            for circuit in c:
                matches = []
                for circ in circuits:
                    if circuit == circ or circuit == circ:
                        matches.append(1)
                for sour in sources:
                    if circuit == sour or circuit == sour:
                        matches.append(1)
                if len(matches) == 0:
                    return (False, 'Circuit id -' + circuit + '- in node -' + node + '- does not correspond to an existent circuit or source...')
        for circuit in circuits:
            c = circuits[circuit]
            f = c['f_id']
            t = c['t_id']
            matches = []
            for node in nodes:
                if f == node:
                    matches.append(1)
                if t == node:
                    matches.append(1)
            if len(matches) == 0:
                return (False, 'Node id -' + node + '- in circuit -' + circuit + '- does not correspond to an existent node...')
        for source in sources:
            c = sources[source]
            f = c['f_id']
            t = c['t_id']
            matches = []
            for node in nodes:
                if f == node:
                    matches.append(1)
                if t == node:
                    matches.append(1)
            if len(matches) == 0:
                return (False, 'Node id -' + node + '- in source -' + source + '- does not correspond to an existent node...')
        return (True, 'Nodes, circuits and sources identifiers are corresponding!')
