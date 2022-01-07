'''
Source definition:
--------------------------------------------------------------------------------
A source represents any connection between two nodes, where there is a voltage
difference and a current is able to flow actively.
'''

from circuit import Circuit

class Voltage(Circuit):

    def __init__(self, name, id, f_id, t_id, voltage, angle, frequency):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str) or not isinstance(f_id, str) or not isinstance(t_id, str) or not isinstance(voltage, flt) or not isinstance(angle, flt) or not isinstance(frequency, flt):
            raise Exception('Parameters name, id, f_id and t_id must be strings ONLY and parameters voltage, angle and frequency must be FLOAT only.')
        # data definition
        self.name = name           # freely user defined circuit public name
        self.id = id               # exclusive identificator (handled elsewhere)
        self.f_id = f_id           # from node identificator
        self.t_id = t_id           # to node identificator
        self.voltage = voltage     # nominal PEAK voltage in Volts
        self.angle = angle         # nominal angle in degrees
        self.frequency = frequency # frequency in Hertz

class Current(Circuit):

    def __init__(self, name, id, f_id, t_id, current, angle, frequency):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str) or not isinstance(f_id, str) or not isinstance(t_id, str) or not isinstance(current, flt) or not isinstance(angle, flt) or not isinstance(frequency, flt):
            raise Exception('Parameters name, id, f_id and t_id must be strings ONLY and parameters current, angle and frequency must be FLOAT only.')
        # data definition
        self.name = name           # freely user defined circuit public name
        self.id = id               # exclusive identificator (handled elsewhere)
        self.f_id = f_id           # from node identificator
        self.t_id = t_id           # to node identificator
        self.current = current     # nominal PEAK current in Amps
        self.angle = angle         # nominal angle in degrees
        self.frequency = frequency # frequency in Hertz
