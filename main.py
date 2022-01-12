# main simulation file

import pandas as pd
import numpy as np

from model.validation import Validation
from model.reader import Reader

from model.impedances import Resistor
from model.impedances import Inductor
from model.impedances import Capacitor

from model.source import Voltage
from model.source import Current

from model.node import Node

def stop(message):
    print('Exiting simulation with message: ' + message)
    exit()

json = 'C:\emtpython\system.json'
validator = Validation(json)
reader = Reader(json)

# validating components

nameValid = validator.validateName()
parametersValid = validator.validateParameters()
nodesValid = validator.validateNodes()
circuitsValid = validator.validateCircuits()
sourcesValid = validator.validateSources()

if not nameValid[0]:
    stop(nameValid[1])

if not parametersValid[0]:
    stop(parametersValid[1])

if not nodesValid[0]:
    stop(nodesValid[1])

if not circuitsValid[0]:
    stop(circuitsValid[1])

if not sourcesValid[0]:
    stop(sourcesValid[1])

# verifing repeated connections

idsChecked = validator.checkIds()

if not idsChecked[0]:
    stop(idsChecked[1])

# processing input data

# transforming json in objects according to existing models

reader.readNodes()
reader.readCircuits()
reader.readSources()
reader.convertSources()

reader.log()

# ending simulation
stop('Simulation finished succesfully!')
