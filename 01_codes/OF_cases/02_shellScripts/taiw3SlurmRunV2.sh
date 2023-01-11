#!/bin/bash
##SBATCH -n 6
#SBATCH -J testOF10
#SBATCH -p ct56                # partition
#SBATCH -t 12:00:00
#SBATCH --account=GOV109092     # computing resource wallet ID
#SBATCH --ntasks=12              # (-n) Number of MPI tasks (i.e. processes)
##SBATCH --cpus-per-task=4       # (-c) Number of cores per MPI task
##SBATCH --ntasks-per-node=4     # Maximum number of tasks on each node
##SBATCH --sockets-per-node=2   # Maximum number of tasks on each socket

# -- Slurm script to run simulations on Taiwania 3

# -- load singularity
module load libs/singularity

# -- run python control
cd ../00_pyCodes
python3 -u caseManagerV1.py