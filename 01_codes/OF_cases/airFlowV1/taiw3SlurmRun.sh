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

# -- load singularity
singDir="/home/u4660703/Singularity/NARLabsInternship/01_codes/singularity/ubuntu.sif"
module load libs/singularity

# -- prepare geometry
singularity exec $singDir bash ./Allrun

# -- run simulation
singularity exec $singDir bash ./Allrun