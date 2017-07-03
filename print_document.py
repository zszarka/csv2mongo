# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 14:51:24 2017

@author: zszarka
"""

import pandas as pd
import numpy as np
from pandas.io.json import json_normalize
from pymongo import MongoClient
import os

f=open("doc_out.txt","a")
#f.write(print_dictionary(document))
def print_dictionary(dictionary,indent=0,out_str=""):
    for key,value in dictionary.items():
        print("\t"*indent + str(key),file=f)
        if isinstance(value,dict):
            print_dictionary(value,indent+1)
        else:
            print("\t"*(indent+1) + str(value),file=f)
            
Client=MongoClient('localhost',27017)
mongo_db=Client.test_db_2
mongo_collection=mongo_db.test

document=mongo_collection.find_one()
print_dictionary(document)

f.close()
