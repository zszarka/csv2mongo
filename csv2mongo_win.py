#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 15:15:01 2017

@author: zsolt
"""
import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from pymongo import MongoClient
import os
import json

def merge(dict1,dict2):
    for d2 in dict2:
        if d2 in dict1 and isinstance(dict1,dict) and isinstance(dict2,dict):
            merge(dict1[d2],dict2[d2])
        else:
            dict1[d2]=dict2[d2]
    return dict1

#directory="Z:\\Lab Book\Zsolt\Copy_From_Lab_Book_Joe\CellProfilerOutput"
#collection_name="test2"
def import_csv(directory,db_name,collection_name):
    Client=MongoClient('localhost',27017)
    mongo_db=Client[db_name]
    mongo_collection=mongo_db[collection_name]
    delete_ret= mongo_collection.delete_many({})
    
    print("Deleted " + str(delete_ret.deleted_count) + " documents")
    
    for fname in os.listdir(directory):
    #    print(fname)
        if fname.endswith(".csv") or fname.endswith(".CSV"):
            filename=os.path.join(directory,fname)
            file=open(filename,"r")
            column_list=file.readline().split(",")
            try:
                insert_count = 0
                failed_insert_count=0
                progress=0
                df=pd.read_csv(filename)
                print("Start Importing " + str(len(df.index)) + " documents from " + filename) 
                for row_num in range(len(df.index)):
                    if int((insert_count * 100) / len(df.index)) > progress:
                        progress = int((insert_count * 100) / len(df.index))
                        print(str(progress)+"%")
                    root=dict()
                    root['Source_File_Name']=fname
                    tree_list=list()
                    for i in range(0,len(column_list)):
                        tree= branch = dict()
                        counter=1
                        j=i
                        column_part_list=column_list[j].split("_")
                        for column_part in column_part_list:
                            if counter==len(column_part_list):
                                if(df[df.columns[j]].dtype == np.int64 ):
                                    branch[column_part]=int(df.iloc[row_num,j])
                                elif (df[df.columns[j]].dtype == np.float64 ):
                                    branch[column_part]=float(df.iloc[row_num,j])
                                else:
        #                            branch[column_part]=list(df.iloc[row_num,j])
                                    branch[column_part]= str(df.iloc[row_num,j]).replace('.','X')
                            else:
                                branch[column_part]={}
                            branch=branch[column_part]
                            counter+=1
                    #    print(tree)
                        tree_list.append(tree)
                        # http://www.w3resource.com/python-exercises/dictionary/python-data-type-dictionary-exercise-27.php
                    
                    for i in range(len(tree_list)):
                        root=merge(root,tree_list[i])
        #            flat_root=json_normalize(root)
            
                    #js_root=json.dumps(root)
                    try:
                        insert_ret=mongo_collection.insert_one(root)
                        insert_count += 1
                    except:
                        failed_insert_count += 1
    #                print("Inserted Document ID: " + str(insert_ret.inserted_id) + " Source_File_Name': " + fname)
                print("Inserted : " + str(insert_count) + " Documents from Source File ': " + fname)
                print("Failed Insert : " + str(failed_insert_count) + " Documents from Source File ': " + fname)
            except:
                    print("File " + str(filename) + " not imported. Invalid Format!")
    #Close connection
    Client.close()

