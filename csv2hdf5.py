#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:14:01 2017

@author: zsolt
"""

"""
Spyder Editor
"""

import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from pymongo import MongoClient
import os
import h5py
#Create an HDF5 File
out_file=h5py.File("mytestfile.hdf5","w")

#filename="C:\\Users\zsolt\Documents\Pipelines\TestOut1\Group_Well_03ALL_Nuclei.csv"
directory="C:\\Users\zsolt\Documents\Pipelines\TestOut1"
for fname in os.listdir("C:\\Users\zsolt\Documents\Pipelines\TestOut1"):
    if fname.endswith(".csv"):
        filename=os.path.join(directory,fname)
        root_group=out_file.create_group(fname)
#        filename_attr=root_group.attrs["File_Name"]=filename
        in_file=open(filename)
        df=pd.read_csv(filename)
        column_list=in_file.readline().split(",")
        
        for i in range(0,len(column_list)):
            dset=out_file.create_dataset(column_list[i].replace("_","/").replace("\n",""),data=df.iloc[:,i])

out_file.close()
#'Source_File_Name': 'Group_Well_03Nuclei.csv'
#'Source_File_Name': 'Group_Well_03Experiment.csv'
