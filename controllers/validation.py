# Input json file validation in programs format

import json as js

class Validation:

    def __init__(self, json):
        # the parameter json is the json file path
        try:
            self.json = js.load(json)
        except:
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
        if not isinstance(p['stop'], flt) or not isinstance(p['dT'], flt) or not isinstance(p['frequency'], flt):
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
            if 'resistance' in c and not isinstance(c['resistance'], flt):
                return (False, 'Circuit resistance is not a float for circuit -> ' + circuit) # resistance is not float
            if 'inductance' in c and not isinstance(c['inductance'], flt):
                return (False, 'Circuit inductance is not a float for circuit -> ' + circuit) # resistance is not float
            if 'capacitance' in c and not isinstance(c['capacitance'], flt):
                return (False, 'Circuit capacitance is not a float for circuit -> ' + circuit) # resistance is not float
        return (True, 'Circuits field is valid!')

    def validateSources(self):
        # opens only the circuits key from the input file
        if ('circuits' not in self.json or self.json['circuits'] == {}):
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
            if 'resistance' in c and not isinstance(c['resistance'], flt):
                return (False, 'Circuit resistance is not a float for circuit -> ' + circuit) # resistance is not float
            if 'inductance' in c and not isinstance(c['inductance'], flt):
                return (False, 'Circuit inductance is not a float for circuit -> ' + circuit) # resistance is not float
            if 'capacitance' in c and not isinstance(c['capacitance'], flt):
                return (False, 'Circuit capacitance is not a float for circuit -> ' + circuit) # resistance is not float
        return (True, 'Circuits field is valid!')
