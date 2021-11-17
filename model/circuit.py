'''
Circuit definition:
--------------------------------------------------------------------------------
A node represents any connection between two nodes, where there is a voltage
difference and a current is able to flow.
'''

# any other class which describes a circuit must inherit from this one

class Circuit:

    def __init__(self, name, id, f_id, t_id):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str) or not isinstance(f_id, str) or not isinstance(t_id, str):
            raise Exception('Parameters name, id, f_id and t_id must be strings ONLY.')
        # data definition
        self.name = name
        self.id = id
        self.f_id = f_id
        self.t_id = t_id

    # the get and set methods were left to Python to handle
