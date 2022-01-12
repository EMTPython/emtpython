# this one effectivelly solves the circuit

import numpy as np
import math

class Solver:

    def __init__(self, data):
        self.data = data

    # steady-state solution
    def steadyState(self):
        # creating G matrix and Z matrix
        G = []
        nodes = self.data['nodes']
        circuits = self.data['circuits']
        for i in range(len(nodes)):
            line = []
            for j in range(len(nodes)):
                m = nodes[i].id
                n = nodes[j].id
                # if m == n, Gmn is the sum of the susceptances connected to node m/n
                if m == n:
                    g = 0
                    for circuit in circuits:
                        if circuit.f_id == m or circuit.t_id == m:
                            if str(type(circuit).__name__) == 'Resistor':
                                g = g + 1 / circuit.resistance
                            if str(type(circuit).__name__) == 'Inductor':
                                g = g + 1 / (1j * 2 * math.pi * self.data['frequency'] * circuit.inductance)
                            if str(type(circuit).__name__) == 'Capacitor':
                                g = g + (1j * 2 * math.pi * self.data['frequency'] * circuit.capacitance)
                    line.append(g)
                else:
                    g = 0
                    for circuit in circuits:
                        if (circuit.f_id == m and circuit.t_id == n) or (circuit.f_id == n and circuit.t_id == m):
                            if str(type(circuit).__name__) == 'Resistor':
                                g = g + 1 / circuit.resistance
                            if str(type(circuit).__name__) == 'Inductor':
                                g = g + 1 / (1j * 2 * math.pi * self.data['frequency'] * circuit.inductance)
                            if str(type(circuit).__name__) == 'Capacitor':
                                g = g + (1j * 2 * math.pi * self.data['frequency'] * circuit.capacitance)
                    line.append(-g)
            G.append(line)
        G = np.matrix(G)
        Z = G.I
        # creating I matrix
        I = []
        sources = self.data['sources'] # assuming the conversion to current sources
        for i in range(len(nodes)):
            m = nodes[i].id
            current = 0
            for source in sources:
                if source.f_id == m:
                    current = current + source.phasor()
                if source.t_id == m:
                    current = current - source.phasor()
            I.append(current)
        I = np.matrix(I)
        I = I.transpose()
        V = Z*I
        voltages = []
        for line in V:
            for v in line:
                voltage = v[0, 0]
                voltage = (math.sqrt(np.real(voltage) ** 2 + np.imag(voltage) ** 2), math.atan(np.imag(voltage) / np.real(voltage)) * 180 / math.pi)
                voltages.append(voltage)
        print(voltages)
