'''
Impedance definition:
--------------------------------------------------------------------------------
An impedance is a circuit which opposes to the flow of current.
'''

from model.circuit import Circuit

class Resistor(Circuit):

    def __init__(self, name, id, f_id, t_id, resistance):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str) or not isinstance(f_id, str) or not isinstance(t_id, str):
            raise Exception('Parameters name, id, f_id and t_id must be strings ONLY.')

        self.name = name   # freely user defined circuit public name
        self.id = id       # exclusive identificator (handled elsewhere)
        self.f_id = f_id   # from node identificator
        self.t_id = t_id   # to node identificator
        self.resistance = resistance

    # method to create an instance from json object
    @staticmethod
    def json(key, value):
        return Resistor(value['name'], key, value['f_id'], value['t_id'], value['resistance'])

class Inductor(Circuit):

    def __init__(self, name, id, f_id, t_id, inductance):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str) or not isinstance(f_id, str) or not isinstance(t_id, str):
            raise Exception('Parameters name, id, f_id and t_id must be strings ONLY.')

        self.name = name   # freely user defined circuit public name
        self.id = id       # exclusive identificator (handled elsewhere)
        self.f_id = f_id   # from node identificator
        self.t_id = t_id   # to node identificator
        self.inductance = inductance

    # method to create an instance from json object
    @staticmethod
    def json(key, value):
        return Inductor(value['name'], key, value['f_id'], value['t_id'], value['inductance'])

class Capacitor(Circuit):

    def __init__(self, name, id, f_id, t_id, capacitance):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str) or not isinstance(f_id, str) or not isinstance(t_id, str):
            raise Exception('Parameters name, id, f_id and t_id must be strings ONLY.')
            
        self.name = name   # freely user defined circuit public name
        self.id = id       # exclusive identificator (handled elsewhere)
        self.f_id = f_id   # from node identificator
        self.t_id = t_id   # to node identificator
        self.capacitance = capacitance

    # method to create an instance from json object
    @staticmethod
    def json(key, value):
        return Capacitor(value['name'], key, value['f_id'], value['t_id'], value['capacitance'])
