from t2listing import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from t2data import *
from mpl_toolkits.mplot3d import Axes3D

liquid_density_kgPm3=1000
water_molecular_weight=0.018
R_value=8.3145
mPmm=1.e-3
dayPs=1./(3600*24)
T_kelven=273.15
T_initial=25.0
P_initial=101.3e3

dat = t2data()
dat.title = 'dp_model_flow'

# #--- set up the model ---------------------------------
length_x = 40.
nblks_x = 80
length_z = 6.
nblks_z = 12
dx = [length_x / nblks_x] * nblks_x
dz = [length_z / nblks_z] * nblks_z
dy = [0.5]
geo = mulgrid().rectangular(dx, dy, dz)
geo.write(dat.title+'.dat')

# #Create TOUGH2 input data file:
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps': 9.99e3,
     'const_timestep': -1,
     'tstop': 100*24*3600,
     'gravity': 9.81,
     'print_level': 2,
     'texp': 1.8,	
     'timestep': [1.0],
     'default_incons': [P_initial, 0.01, 10.99, T_initial, None]})
	 
dat.parameter['print_interval']=dat.parameter['max_timesteps']/20
dat.parameter['max_timestep']=dat.parameter['tstop']/dat.parameter['max_timesteps']

dat.start = True
#dat.diffusion=[[2.13e-5,     0.e-8],   [2.13e-5,     0.e-8]]
dat.multi={'num_components': 3, 'num_equations': 3, 'num_phases': 3, 'num_secondary_parameters': 6}
dat.selection={'float':[0.8,0.8,None, None, None, None, None, None],'integer':[1, None, None, None, None, None, None, None, None, 1, 3, 0, 0, 0, 0, 1]}

# #Set MOPs:
dat.parameter['option'][1] = 1
dat.parameter['option'][7] = 0
dat.parameter['option'][11] = 0
dat.parameter['option'][16] = 4
dat.parameter['option'][19] = 2
dat.parameter['option'][21] = 3

# #Add another rocktype, with relative permeability and capillarity functions & parameters:
r1 = rocktype('SAND ', nad=2, porosity=0.45,density=2650.,permeability = [2.e-12, 2.e-12, 2.e-12],conductivity=2.51,specific_heat=920)
r1.tortuosity=0
dat.grid.add_rocktype(r1)
r1.relative_permeability = {'type': 7, 'parameters': [0.627, 0.045, 1., 0.054]}
r1.capillarity = {'type': 7, 'parameters': [0.627, 0.045, 5.e-4, 1.e8, 1.]}

r2 = rocktype('BOUND', nad=2,porosity=0.99,density=2650., permeability = [2.e-12, 2.e-12, 2.e-12],conductivity=2.51,specific_heat=1.e5)
dat.grid.add_rocktype(r2)
r2.relative_permeability = {'type': 1, 'parameters': [0.1, 0., 1., 0.1]}
r2.capillarity = {'type': 1, 'parameters': [0., 0., 1.0]}
		
bvol = 0.0
conarea = dy[0] * dz[0]
condist = 1.e-10
# #assign rocktype and parameter values:
for blk in dat.grid.blocklist:
    blk.rocktype = r1
    blk.ahtx=conarea

# #add boundary condition block at each end:
for i in range(nblks_z):
    b1 = t2block('zzz'+str(i+1), bvol, r2)
    b1.volume=1.e50
    dat.grid.add_block(b1)
    con1 = t2connection([b1, dat.grid.blocklist[i*nblks_x],b1],
                    distance = [condist,0.5*dx[0]], area = conarea, direction=1)
    dat.grid.add_connection(con1)
    dat.grid.connectionlist[-1].dircos=0
    dat.grid.blocklist[-1].ahtx=conarea
    dat.grid.blocklist[-1].centre=np.array([0,0.25,-(length_z/nblks_z+i)/2])

for i in range(nblks_z-4):
    b2 = t2block('zzz'+str(nblks_z+i+1), bvol, dat.grid.rocktype['BOUND'])
    b2.volume=1.e50
    dat.grid.add_block(b2)
    con2 = t2connection([dat.grid.blocklist[nblks_x-1+(i+4)*nblks_x], b2],
                    distance = [0.5*dx[nblks_x-1], condist], area = conarea, direction=1)
    dat.grid.add_connection(con2)
    dat.grid.connectionlist[-1].dircos=0
    dat.grid.blocklist[-1].ahtx=conarea
    dat.grid.blocklist[-1].centre=np.array([length_x,0.25,-(length_z/nblks_z+i+4)/2])

# #Set initial condition:
for i in range(nblks_z-4):
    dat.incon[str(dat.grid.blocklist[-(i+1)])] = [None, [P_initial-liquid_density_kgPm3*dat.parameter['gravity']*(dat.grid.blocklist[-(i+1)].centre[2]+2), 0.25, 10.01, T_initial]]
for i in range(nblks_z):
    dat.incon[str(dat.grid.blocklist[-(i+1+nblks_z-4)])] = [None, [P_initial-liquid_density_kgPm3*dat.parameter['gravity']*(dat.grid.blocklist[-(i+1+nblks_z-4)].centre[2]+1.5), 0.01, 10.01, T_initial]]

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

# # #Set initial condition:


# # #add generator:
# flow_rate_mmPday=-5
# flow_rate_kgPs=flow_rate_mmPday*conarea*liquid_density_kgPm3*mPmm*dayPs
# gen = t2generator(name = 'INF 1', block = dat.grid.blocklist[0].name,
                  # gx = flow_rate_kgPs, type = 'COM1')
# dat.add_generator(gen)


# #--- write TOUGH2 input file ------------------------------------	
dat.write(dat.title)