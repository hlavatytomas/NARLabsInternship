# -- Python script to create manage openFoam cases using python class OpenFOAMCase

# -- for the usage see please OF_caseClass.py

# -- imports 
from OF_caseClass import OpenFOAMCase

# -- parameters 
bsCsDir = "../01_baseCaseV2"
finCsDir = "../ZZ_cases/hongKongV1"

# -- blockMesh parameters
DOMAIN_SIZE_X = 420*2
DOMAIN_SIZE_Y = 270*2
DOMAIN_SIZE_MX = -80*2
DOMAIN_SIZE_MY = -30*2
DOMAIN_SIZE_Z = 300*2 
NC_X = 75
NC_Y = 45
NC_Z = 60
REF_LEVEL_VELKY_BOX = 2

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
            ["system/snappyHexMeshDict", "REF_LEVEL_VELKY_BOX", str(REF_LEVEL_VELKY_BOX)],
        ]
}   

# -- prepare case
hk1 = OpenFOAMCase()
hk1.loadOFCaseFromBaseCase(bsCsDir)
hk1.changeOFCaseDir(finCsDir)
hk1.copyBaseCase()
for replace in changes["replaces"]:
    hk1.replace(replace)

# NOTE: not used for my PC
# # -- create geometry and run simulation on my PC
# hk1.runCommands(
#     [
#         "bash ./geometry",
#         "bash ./simulationFlow", 
#         "bash ./simulationPollution"
#     ])     

# -- create geometry and run flow simulation on Kuos desktop
hk1.runCommands \
(
    [
        "chmod 775 -R ./*",
        "singularity exec -H %s/%s ~/Singularity/ubuntu2.sif bash ./geometry" % (hk1.whereIStart,hk1.dir),
        "singularity exec -H %s/%s ~/Singularity/ubuntu2.sif bash ./simulationFlow" % (hk1.whereIStart,hk1.dir),
    ]
) 

# # -- update OpenFOAMCase.times variable, copy initial condition for pollution simulation, and run pollution simulation
# hk1.updateTimes()
# flLt = hk1.latestTime
# hk1.setParameter()
# hk1.runCommands \
# (
#     [
#         "cp -r 0/yPol %g/" %(hk1.latestTime),
#         "singularity exec -H %s/%s ~/Singularity/ubuntu2.sif bash ./simulationPollution" % (hk1.whereIStart,hk1.dir),
#     ]
# )

# # -- update times variable and copy pressure field into latestTime for visualizations
# hk1.updateTimes()
# hk1.runCommands \
# (
#     [
#         "cp -r %g/p %g/" %(flLt, hk1.latestTime),
#     ]
# )

        
     