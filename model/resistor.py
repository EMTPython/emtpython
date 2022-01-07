'''
Resistor definition:
--------------------------------------------------------------------------------
A resistor is a circuit which converts electrical energy in thermal energy. It
opposes to the flow of current.
'''

from circuit import Circuit

class Resistor(Circuit):

    def __init__(self, name, id, f_id, t_id, resistance):
        super().__init__(self, name, id, f_id, t_id)
        self.resistance = resistance
