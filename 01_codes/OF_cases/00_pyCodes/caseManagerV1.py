# -- Python script to create manage openFoam cases using python class OpenFOAMCase

# -- for the usage see please OF_caseClass.py

# -- imports 
from OF_caseClass import OpenFOAMCase

# -- parameters 
bsCsDir = "../01_baseCaseV2/"
finCsDir = "../ZZ_cases/hongKongV1/"

# -- load base case
hk1 = OpenFOAMCase()
hk1.loadOFCaseFromBaseCase(bsCsDir)
hk1.changeOFCaseDir(finCsDir)
hk1.copyBaseCase()
hk1.runCommand(["ls"])

