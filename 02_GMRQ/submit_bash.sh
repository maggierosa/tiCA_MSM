#!/bin/bash

n_cluster="50 100 150 200 250 300 350 400 450 500"
# The number of microstates you want to test out 

for i in $n_cluster
do
        sbatch submit.sh $i
done
