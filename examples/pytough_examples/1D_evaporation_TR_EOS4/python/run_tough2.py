
from t2listing import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
import time
from t2data import *
from mpl_toolkits.mplot3d import Axes3D

#--- run the model ------------------------------------

# delete exisiting input file
cwd=os.getcwd()
inp_path=os.path.join(os.getcwd(),inp.title)

if os.path.exists(inp_path):
    os.remove(inp_path)
    print("Existing "+ "flow.out" + " deleted\n")
else:
    print("Can not delete "+ "flow.out" + "  as it doesn't exists\n")

t = time.time()
#os.system(" tough2 -to sam6_0.listing sam6 4")
#os.system(' tough2 -to '+dat.title+'.listing '+dat.title+' 4')
#os.system(' itough2 -tough2 '+dat.title+'.listing '+dat.title+' 4')
os.system('treactv2087_eos4_gf')
elapsed = time.time() - t
print('Simulation Elapsed: %s minutes' %(elapsed/60))
