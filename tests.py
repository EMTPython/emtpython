# testing node and circuit models

from model.node import Node
from model.circuit import Circuit

try:
    node = Node('bus', '40028922')
    grnd = Node.ground()
    circuit = Circuit('line', '05001234505', '40028922', '0')
    print(node, grnd, circuit)
except Exception as error:
    print(error)
