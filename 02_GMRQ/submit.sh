#!/bin/bash -l
#SBATCH -A bip109    # charge this account
#SBATCH -t 0-24:0:0   # days-hours:minutes:seconds
#SBATCH -N 2         # = ceiling ( # of directories / 32 )


conda activate /ccs/home/margaridarosa/msmbuilder

python msm.py $1 #COMMENT after, Run First  

#python gmrq.py $1 #UNCOMMENT Run Second 

exit
