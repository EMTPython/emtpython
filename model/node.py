'''
Node or bus definition:
--------------------------------------------------------------------------------
A node represents a region between two or more circuit elements, with negligible
resistance, so there is no voltage difference.
'''

class Node:

    def __init__(self, name, id, circuits = []):
        # data checking
        if not isinstance(name, str) or not isinstance(id, str):
            raise Exception('Parameters name and id must be strings ONLY.')
        # data definition
        self.name = name          # freely user defined node public name
        self.id = id              # exclusive identificator (handled elsewhere)
        self.circuits = circuits  # connected circuits identifiers

    def log(self):
        print('Node with id: ' + self.id + '; name: ' + self.name + '; circuits: ' + str(len(self.circuits)))    

    # the get and set methods were left for Python to handle

    # method to create a ground node
    @staticmethod
    def ground():
        return Node('ground', '0')

    # method to create an instance from json object
    @staticmethod
    def json(key, value):
        return Node(value['name'], key, value['circuits'])
