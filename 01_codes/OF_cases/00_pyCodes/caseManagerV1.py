# -- Python script to create manage openFoam cases using python class OpenFOAMCase

# -- for the usage see please OF_caseClass.py

# -- imports 
from OF_caseClass import OpenFOAMCase

# -- parameters 
bsCsDir = "../01_baseCaseV2/"
finCsDir = "../ZZ_cases/hongKongV1/"

# -- blockMesh parameters
DOMAIN_SIZE_X = 420*2
DOMAIN_SIZE_Y = 270*2
DOMAIN_SIZE_MX = -80*2
DOMAIN_SIZE_MY = -30*2
DOMAIN_SIZE_Z = 300*2 
NC_X = 150
NC_Y = 90
NC_Z = 120

# -- changes that should be applied
changes = \
{
    "replaces": 
        [
            ["system/blockMeshDict", "DOMAIN_SIZE_X", str(DOMAIN_SIZE_X)],
            ["system/blockMeshDict", "DOMAIN_SIZE_Y", str(DOMAIN_SIZE_Y)],
            ["system/blockMeshDict", "DOMAIN_SIZE_Z", str(DOMAIN_SIZE_Z)],
            ["system/blockMeshDict", "DOMAIN_SIZE_MX", str(DOMAIN_SIZE_MX)],
            ["system/blockMeshDict", "DOMAIN_SIZE_MY", str(DOMAIN_SIZE_MY)],
            ["system/blockMeshDict", "NC_X", str(NC_X)],
            ["system/blockMeshDict", "NC_Y", str(NC_Y)],
            ["system/blockMeshDict", "NC_Z", str(NC_Z)],
        ]
}   

# -- load base case
hk1 = OpenFOAMCase()
hk1.loadOFCaseFromBaseCase(bsCsDir)
hk1.changeOFCaseDir(finCsDir)
hk1.copyBaseCase()
for replace in changes["replaces"]:
    hk1.replace(replace)
hk1.runCommands(["sh ./geometry"])

