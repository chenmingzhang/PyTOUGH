
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
out_path=os.path.join(os.getcwd(),'flow.out')
chemical_out_path=os.path.join(os.getcwd(),'chemical.out')
runlog_path=os.path.join(os.getcwd(),'runlog.out')
chdump_path=os.path.join(os.getcwd(),'chdump.out')
solute_path=os.path.join(os.getcwd(),'solute.out')


if os.path.exists(out_path):
    os.remove(out_path)
    print("Existing "+ "flow.out, "+"chemical.out, "+ "runlog.out, "+"chdump.out, "+"solute.out,"  + " deleted\n")
else:
    print("Can not delete "+ "flow.out" + "  as it doesn't exists\n")

if os.path.exists(chemical_out_path):
    os.remove(chemical_out_path)
    print("Existing "+ "flow.out, "+"chemical.out, "+ "runlog.out, "+"chdump.out, "+"solute.out,"  + " deleted\n")
else:
    print("Can not delete "+ "flow.out" + "  as it doesn't exists\n")

if os.path.exists(runlog_path):
    os.remove(runlog_path)
    print("Existing "+ "flow.out, "+"chemical.out, "+ "runlog.out, "+"chdump.out, "+"solute.out,"  + " deleted\n")
else:
    print("Can not delete "+ "flow.out" + "  as it doesn't exists\n")

if os.path.exists(chdump_path):
    os.remove(chdump_path)
    print("Existing "+ "flow.out, "+"chemical.out, "+ "runlog.out, "+"chdump.out, "+"solute.out,"  + " deleted\n")
else:
    print("Can not delete "+ "flow.out" + "  as it doesn't exists\n")

if os.path.exists(chdump_path):
    os.remove(solute_path)
    print("Existing "+ "flow.out, "+"chemical.out, "+ "runlog.out, "+"chdump.out, "+"solute.out,"  + " deleted\n")
else:
    print("Can not delete "+ "flow.out" + "  as it doesn't exists\n")





t = time.time()
#os.system(" tough2 -to sam6_0.listing sam6 4")
#os.system(' tough2 -to '+dat.title+'.listing '+dat.title+' 4')
#os.system(' itough2 -tough2 '+dat.title+'.listing '+dat.title+' 4')
os.system('treactv2087_eos4_gf')
elapsed = time.time() - t
print('Simulation Elapsed: %s minutes' %(elapsed/60))
