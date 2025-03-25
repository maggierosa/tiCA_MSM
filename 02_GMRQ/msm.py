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
import msmbuilder
import msmbuilder.decomposition.tica as ti
from msmbuilder.cluster import KMeans, KCenters
from msmbuilder.msm import ContinuousTimeMSM, MarkovStateModel
from msmbuilder.msm import implied_timescales


n_cluster=sys.argv[1]
print(n_cluster)

df_first3=[]
for i in range(912):
    test=np.load('/lustre/orion/bip109/scratch/margaridarosa/MFSD2A_WT_Frontier_OpenMM_Ensemble/collective_variables_for_tica_ions_lpc_and_protein/tica/proj_combined_WT_Li_CV_3d_%d.npy' %i) # MODIFY PATH 
    df_first3.append(test[:,:3])

print(df_first3[1].shape)
cluster=KMeans(n_clusters=int(n_cluster),n_jobs=-1,verbose=0,max_iter=100,tol=.0001)
cluster.fit(df_first3)

for i in range(912): # Number of Total Trajectories 
    np.savetxt('assigns_%sstates_%d_3d.txt' %(n_cluster,i),cluster.labels_[i],fmt='%1d')
np.savetxt('microstate_centers_%sstates_3d.txt' %n_cluster,cluster.cluster_centers_) # Output 
