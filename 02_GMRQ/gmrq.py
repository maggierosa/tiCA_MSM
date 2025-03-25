# Imports 
# Make sure these are all in your environment 

import numpy as np
import matplotlib.pyplot as plt
import mdtraj.io as io
import matplotlib
from sklearn.cluster import KMeans
import pandas as pd
import os,sys,glob

matplotlib.use('Agg')
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
from matplotlib import rcParams
import matplotlib.cm as cm

import msmbuilder
import msmbuilder.decomposition.tica as ti
from msmbuilder.cluster import KMeans, KCenters
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from msmbuilder.msm import implied_timescales

# User Inputs 
n_cluster=sys.argv[1]
print(n_cluster)
lag_time=100
dataset=[]
n_tests = 500

# Do not modify anything below this line 

traj_list=np.arange(0,912)
set_set_ratio=4
listofspecial=np.array([])
othertrajs=np.setdiff1d(traj_list,listofspecial)

n_special = int(len(listofspecial)/set_set_ratio)
n_others = int(len(othertrajs)/set_set_ratio) #all 312 trajs unless specified in n_special

sequences = []
for i in traj_list:
    sequences.append(np.loadtxt('assigns_%sstates_%d_3d.txt' %(n_cluster,i),dtype=int))

GMRQscore = np.zeros(n_tests)
for test in range(n_tests):
    testset_special = np.array([])
    trainset_special = np.array([])
    #print(len(listofspecial))
    testset_others = np.unique(np.random.choice(othertrajs,n_others,replace=False))
    trainset_others = np.setdiff1d(othertrajs,testset_others)
    if len(listofspecial)!=0:
        testset_special = np.unique(np.random.choice(listofspecial,n_special,replace=False))
        trainset_special = np.setdiff1d(listofspecial,testset_special)

    testset = np.unique(np.concatenate((testset_others,testset_special))).astype(int)
    trainset = np.unique(np.concatenate((trainset_others,trainset_special))).astype(int)

    train_seq = []
    for i in trainset:
        index = np.where(traj_list==i)[0][0]
        train_seq.append(sequences[index])
    test_seq = []
    for i in testset:
        index = np.where(traj_list==i)[0][0]
        test_seq.append(sequences[index])

    msm = MarkovStateModel(lag_time=lag_time, n_timescales=30, reversible_type='transpose', ergodic_cutoff='off', prior_counts=0, sliding_window=True, verbose=True)
    msm.fit(train_seq)
    GMRQscore[test]=msm.score(test_seq)


np.savetxt("GMRQscore_3d_%s_l%d.txt"%(n_cluster,lag_time),GMRQscore,fmt='%.4f')
