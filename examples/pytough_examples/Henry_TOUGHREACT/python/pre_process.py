from t2listing import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
#from t2data import *
from mpl_toolkits.mplot3d import Axes3D
import importlib
import py_compile
cwd = os.getcwd()



# reload t2listing and t2data in case there is update in the module 
pytough_path=os.environ['pytough']
print(os.environ['pytough'])

current_path=os.getcwd()
current_folder_name=os.path.basename(current_path)
sys.path.append(os.path.join(pytough_path,'python'))

py_compile.compile(os.path.join(pytough_path,'python','t2listing.py'))
py_compile.compile(os.path.join(pytough_path,'python','t2data.py'))

import t2listing
import t2data
importlib.reload(t2listing)
importlib.reload(t2data)


liquid_density_kgPm3   = 1000
brine_density_kgPm3    = 1185.1
water_molecular_weight = 0.018
R_value                = 8.3145
mPmm                   = 1.e-3
dayPs                  = 1./(3600*24)
T_kelven               = 273.15
T_initial              = 25.0
P_initial              = 101.3e3

dat       = t2data.t2data()
dat.title = 'flow.inp'   # for toughreact, only 'flow.inp' can be used as flow input file
dat.add_react(mopr=[None,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])
# the first 2 means only run tough2 not chemical and solute

# #--- set up the model ---------------------------------
length_x = 40.
nblks_x  = 80
length_z = 6.
nblks_z  = 12
dx       = [length_x / nblks_x] * nblks_x
dz       = [length_z / nblks_z] * nblks_z
dy       = [0.5]
geo      = t2data.mulgrid().rectangular(dx, dy, dz)
geo.write(dat.title+'.dat')

# #Create TOUGH2 input data file:
dat.grid = t2data.t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps'  : 9.e3,
     'const_timestep' : -1,
     'tstop'          : 200*24*3600,
     'gravity'        : 9.81,
     'print_level'    : 2,
     'texp'           : 1.8,
     'timestep'       : [1.0],
     'default_incons' : [P_initial, 0, 10.99, T_initial, None]})
	 
dat.parameter['print_interval'] = dat.parameter['max_timesteps']/20
dat.parameter['max_timestep']   = dat.parameter['tstop']/dat.parameter['max_timesteps']

# #Set MOPs:
dat.parameter['option'][1]  = 1
dat.parameter['option'][7]  = 0
dat.parameter['option'][11] = 0
dat.parameter['option'][16] = 4
dat.parameter['option'][19] = 2
dat.parameter['option'][21] = 3

dat.start = True
#dat.diffusion=[[2.13e-5,     0.e-8],   [2.13e-5,     0.e-8]]
dat.multi={'num_components': 3, 'num_equations': 3, 'num_phases': 2, 'num_secondary_parameters': 6}
dat.selection={'float':[None],'integer':[2]}

# #Add another rocktype, with relative permeability and capillarity functions & parameters:
r1                       = t2data.rocktype('SAND ', nad = 2, porosity = 0.45,density = 2650.,permeability = [2.e-12, 2.e-12, 2.e-12],conductivity = 2.51,specific_heat = 920)
r1.tortuosity            = 0
r1.relative_permeability = {'type': 7, 'parameters': [0.627, 0.045, 1., 0.054]      }
r1.capillarity           = {'type': 7, 'parameters': [0.627, 0.045, 5.e-4, 1.e8, 1.]}
dat.grid.add_rocktype(r1)

r2                       = t2data.rocktype('BOUND', nad = 2,porosity = 0.99,density = 2650., permeability = [2.e-12, 2.e-12, 2.e-12],conductivity = 2.51,specific_heat = 1.e5)
r2.relative_permeability = {'type': 1, 'parameters': [0.1, 0., 1., 0.1]}
r2.capillarity           = {'type': 1, 'parameters': [0. , 0., 1.0    ]}
dat.grid.add_rocktype(r2)
# relative_humidity=0.1
# P_bound=np.log(relative_humidity)*liquid_density_kgPm3*R_value*(T_initial+T_kelven)/water_molecular_weight
# r2.relative_permeability = {'type': 1, 'parameters': [0.1,0.0,1.0,0.1,]}
# r2.capillarity = {'type': 1, 'parameters': [-P_bound, 0., 1.0]}
	
bvolume = 1.e50
conarea = dy[0] * dz[0]
condist = 1.e-10
# #assign rocktype and parameter values:
for blk in dat.grid.blocklist:
    blk.rocktype = r1
    blk.ahtx=conarea

# #add boundary condition block at each end:
for i in range(nblks_z):
    b1 = t2data.t2block('zzz'+str(i+1), bvolume, dat.grid.rocktype['BOUND'],ahtx=conarea,centre=np.array([0,0.25,-(length_z/nblks_z+i)/2]) )
    dat.grid.add_block(b1)
    con1 = t2data.t2connection([b1, dat.grid.blocklist[i*nblks_x],b1],                     # why three
                    distance = [condist,0.5*dx[0]], area = conarea, direction=1)    #dirction=1 ends up with betax=0 (cos between gravity and line between link)
    dat.grid.add_connection(con1)

for i in range(nblks_z-4):
    b2 = t2data.t2block('zzz'+str(nblks_z+i+1), bvolume, dat.grid.rocktype['BOUND'],ahtx=conarea,centre=np.array([length_x,0.25,-(length_z/nblks_z+i+4)/2]))
    dat.grid.add_block(b2)
    con2 = t2data.t2connection([dat.grid.blocklist[nblks_x-1+(i+4)*nblks_x], b2],
                    distance = [0.5*dx[nblks_x-1], condist], area = conarea, direction=1)
    dat.grid.add_connection(con2)


#for i in range(nblks_z-4):
#    #print(dat.grid.blocklist[-(i+1)])
#    print(brine_density_kgPm3*dat.parameter['gravity']*(dat.grid.blocklist[-(i+1)].centre[2]+1.5)

# #Set initial condition:
for i in range(nblks_z-4):
    dat.incon[str(dat.grid.blocklist[-(i+1)])] = \
        [None, [P_initial-brine_density_kgPm3*dat.parameter['gravity']*(dat.grid.blocklist[-(i+1)].centre[2]+1.5), 1, 10.01, T_initial]]

#[None, [144896.86625, 1, 10.01, 25.0]]

for i in range(nblks_z):
    dat.incon[str(dat.grid.blocklist[-(i+1+nblks_z-4)])] \
        = [None, [P_initial-liquid_density_kgPm3*dat.parameter['gravity']*(dat.grid.blocklist[-(i+1+nblks_z-4)].centre[2]+1), 0, 10.01, T_initial]]

# #deleted block:
j=0
i=(10*2-1)*(j+1)+j*10
while i<nblks_x*(j+1)-((nblks_x-(10*2-1))*j):
    dat.grid.delete_block(str(dat.grid.blocklist[(10*2-1)*(j+1)+j*10]))
    i+=1
	
j=1
i=(10*2-1)*(j+1)+j*10
while i<nblks_x*(j+1)-((nblks_x-(10*2-1))*j):
    dat.grid.delete_block(str(dat.grid.blocklist[(10*2-1)*(j+1)+j*10]))
    i+=1

j=2
i=(10*2-1)*(j+1)+3*10
while i<nblks_x*(j+1)-((nblks_x-(10*2-1))*j-10):
    dat.grid.delete_block(str(dat.grid.blocklist[(10*2-1)*(j+1)+3*10]))
    i+=1

j=3
i=(10*2-1)*(j+1)+6*10
while i<nblks_x*(j+1)-((nblks_x-(10*2-1))*j-10*3):
    dat.grid.delete_block(str(dat.grid.blocklist[(10*2-1)*(j+1)+6*10]))
    i+=1


# # #add generator:
# flow_rate_mmPday=-5
# flow_rate_kgPs=flow_rate_mmPday*conarea*liquid_density_kgPm3*mPmm*dayPs
# gen = t2generator(name = 'INF 1', block = dat.grid.blocklist[0].name,
                  # gx = flow_rate_kgPs, type = 'COM1')
# dat.add_generator(gen)

# #--- write TOUGH2 input file ------------------------------------	
dat.write(dat.title)
