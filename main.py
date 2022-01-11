# main simulation file

import pandas as pd
import numpy as np

from controllers.validation import Validation

def stop(message):
    print('Exiting simulation with message: ' + message)
    exit()

json = 'C:\emtpython\system.json'
validator = Validation(json)

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

# proccessing input data

# transforming json in objects according to existing models

# ending simulation
stop('Simulation finished succesfully!')
