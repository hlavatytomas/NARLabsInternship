# -- Python script to create manage openFoam cases using python class OpenFOAMCase

# -- for the usage see please OF_caseClass.py

# -- imports 
import numpy as np
import os
from OF_caseClass import OpenFOAMCase

# -- parameters 
bsCsDir = "../airFlowV2"

# -- load base case
myBaseCase = OpenFOAMCase()
myBaseCase.loadOFCaseFromBaseCase(bsCsDir)

