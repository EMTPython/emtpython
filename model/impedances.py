'''
Impedance definition:
--------------------------------------------------------------------------------
An impedance is a circuit which opposes to the flow of current.
'''

from circuit import Circuit

class Resistor(Circuit):

    def __init__(self, name, id, f_id, t_id, resistance):
        super().__init__(self, name, id, f_id, t_id)
        self.resistance = resistance

class Resistor(Circuit):

    def __init__(self, name, id, f_id, t_id, inductance):
        super().__init__(self, name, id, f_id, t_id)
        self.inductance = inductance

class Capacitance(Circuit):

    def __init__(self, name, id, f_id, t_id, capacitance):
        super().__init__(self, name, id, f_id, t_id)
        self.inductance = capacitance
