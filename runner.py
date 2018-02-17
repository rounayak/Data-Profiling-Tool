from __future__ import print_function
from an import looper
import os
loca=os.getcwd()
path=os.getcwd()+'\\output'
try:
    os.stat(path)
except:
 os.mkdir(path) 
import os
lister=[]
files=[x for x in os.listdir() if 'csv' in x]
for i in files:
    files2=[x for x in files if i not in x]
    for j in files2:
        looper(i,j,loca)
        os.chdir(loca)
os.chdir(loca)        
        





