'''
Circuit definition:
--------------------------------------------------------------------------------
A circuit represents any connection between two nodes, where there is a voltage
difference and a current is able to flow.
'''

# any other class which describes a circuit must inherit from this one

class Circuit:

    def __init__(self, name, id, f_id, t_id):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str) or not isinstance(f_id, str) or not isinstance(t_id, str):
            raise Exception('Parameters name, id, f_id and t_id must be strings ONLY.')
        # data definition
        self.name = name   # freely user defined circuit public name
        self.id = id       # exclusive identificator (handled elsewhere)
        self.f_id = f_id   # from node identificator
        self.t_id = t_id   # to node identificator

    # the get and set methods were left to Python to handle
