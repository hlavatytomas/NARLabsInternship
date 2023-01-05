#!/bin/bash
##SBATCH -n 6
#SBATCH -J testOF10
#SBATCH -p ctest                # partition
#SBATCH --account=GOV109092     # computing resource wallet ID
#SBATCH --ntasks=6              # (-n) Number of MPI tasks (i.e. processes)
##SBATCH --cpus-per-task=4       # (-c) Number of cores per MPI task
##SBATCH --ntasks-per-node=4     # Maximum number of tasks on each node
##SBATCH --sockets-per-node=2   # Maximum number of tasks on each socket

# -- Slurm script to run simulations on Taiwania 3

# -- parameters for script
# singularity image file
singDir="../../singularity/ubuntu.sif"¨

# openFoam case dir
caseDir="../airFlowV1"

# -- load singularity
module load libs/singularity

# -- run scripts that are listed in script parameters
i=1;
for scriptToRun in "$@" 
do
    # echo "Username - $i: $user";
    singularity exec $singDir bash $caseDir/$scriptToRun
    i=$((i + 1));
done

# -- prepare geometry
# singularity exec $singDir bash $caseDir/Allrun

# -- run simulation
# singularity exec $singDir bash $caseDir/Allrun2