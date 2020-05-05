from t2listing import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from t2data import *
from mpl_toolkits.mplot3d import Axes3D

liquid_density_kgPm3   = 1000
water_molecular_weight = 0.018
R_value                = 8.3145
mPmm                   = 1.e-3
dayPs                  = 1./(3600*24)
T_init_c               = 25.0
p_atm_pa               = 101.3e3

dat       = t2data()
dat.title = 'flow.inp'

# #--- set up the model ---------------------------------
length = 1.
nblks  = 50
dz     = [length / nblks] * nblks
dy     = dx  = [0.1]
geo    = mulgrid().rectangular(dx, dy, dz)
#geo   = mulgrid().rectangular(dx, dy, dz, atmos_type = 0)
#geo.write(dat.title+'.dat')

# #Create TOUGH2 input data file:
dat.grid = t2grid().fromgeo(geo)
dat.parameter.update(
    {'max_timesteps'  : 3.e3,
     'const_timestep' : -1,
     'tstop'          : 360*24*3600,
     'gravity'        : 9.81,
     'print_level'    : 2,      #-3
     'texp'           : 2.41e-05,
     'timestep'       : [1.0],
     'be'             : 2.334,
     'default_incons' : [p_atm_pa, 10.99, T_init_c, None],
     'relative_error' : 1.e-5})
	 
dat.parameter['print_interval'] = dat.parameter['max_timesteps']/20
dat.parameter['max_timestep']   = dat.parameter['tstop']/dat.parameter['max_timesteps']

dat.start = True
dat.diffusion=[[2.13e-5,     0.e-8],   [2.13e-5,     0.e-8]]
dat.multi={ 'num_components'           : 2,   # warning, the key needs to be exactly the same, no extra spacings
            'num_equations'            : 3,
            'num_phases'               : 2,
            'num_secondary_parameters' : 8}

# #Set MOPs:
dat.parameter['option'][1]  = 1
dat.parameter['option'][7]  = 0
dat.parameter['option'][9]  = 1
dat.parameter['option'][11] = 0
dat.parameter['option'][16] = 4
dat.parameter['option'][19] = 2
dat.parameter['option'][21] = 3

# #Add another rocktype, with relative permeability and capillarity functions & parameters:
r1 = rocktype('SAND ', 
        nad           = 2,
        porosity      = 0.45,
        density       = 2650.,
        permeability  = [2.e-12, 2.e-12, 2.e-12],
        conductivity  = 2.51,
        specific_heat = 920)
Residual_saturation      = 0.045
r1.relative_permeability = {'type': 7, 'parameters': [0.627, Residual_saturation, 1., 0.054]}
r1.capillarity           = {'type': 7, 'parameters': [0.627, Residual_saturation-1.e-5, 5.e-4, 1.e8, 1.]}
dat.grid.add_rocktype(r1)
	
r2 = rocktype('BOUND',
        nad           = 2,
        porosity      = 0.99,
        density       = 2650.,
        permeability  = [2.e-12, 2.e-12, 2.e-12],
        conductivity  = 2.51,
        specific_heat = 1.e5)
r2.relative_permeability = {'type': 1, 'parameters': [0.1,0.0,1.0,0.1,]}
r2.capillarity           = {'type': 1, 'parameters': [0., 0., 1.0]}
dat.grid.add_rocktype(r2)


bvol    = 1.e50
conarea = dx[0] * dy[0]
condist = 1.e-10
  
# #assign rocktype and parameter values:
for blk in dat.grid.blocklist:
    blk.rocktype = r1
    blk.ahtx     = conarea   # interface area for heat exchange
	
# #add boundary condition block at each end:
b1 = t2block('bdy01', bvol, r2,
             ahtx      = conarea)# area for heat exchange 
#dat.grid.add_block(b1)

dat.grid.blocklist.insert(0,b1)
#del dat.grid.blocklist[-1]


con1 = t2connection([dat.grid.block['  a 1'],b1],
                    distance  = [0.5*dz[0],condist],
                    area      = conarea, 
                    direction = 3,   # which to read permeability
                    dircos    = -1)  # ISOT not BETX
#dat.grid.add_connection(con1)

dat.grid.connectionlist.insert(0,con1)


# b2 = t2block('bdy02', bvol, dat.grid.rocktype['BOUND'])
# dat.grid.add_block(b2)
# con2 = t2connection([dat.grid.blocklist[nblks-1], b2],
                    # distance = [0.5*dz[nblks-1], condist], area = conarea, direction=3)
# dat.grid.add_connection(con2)


## #Set initial condition:
#for i in range(len(dat.grid.blocklist)-1):
#    dat.incon[str(dat.grid.blocklist[i])] = \
#            [None, [p_atm_pa+dat.grid.blocklist[i].centre[2]*(-1)*liquid_density_kgPm3*dat.parameter['gravity'], 10.01, 25.0]]

for num,key in enumerate(dat.grid.blocklist):
    if str(key)[:3]=='  a':
        dat.incon[str(key)] = \
                [None, [p_atm_pa - dat.grid.block[str(key)].centre[2]*liquid_density_kgPm3*dat.parameter['gravity'], 10.01, T_init_c]]
                #[None, [p_atm_pa+dat.grid.block[str(key)].centre[2]*(-1)*liquid_density_kgPm3*dat.parameter['gravity'], 10.01, T_init_c]]

dat.incon['bdy01'] = [None, [p_atm_pa, 0.99, T_init_c]]   # what does 0.99 mean?
dat.incon['  a 2'][1][1] = 10.99                          # why is this needed?



# #add generator:
flow_rate_mmPday = -5.
flow_rate_kgPs   = flow_rate_mmPday*conarea*liquid_density_kgPm3*mPmm*dayPs
gen              = t2generator(name  = 'INF 1', 
                               block = '  a 1',      #dat.grid.blocklist[0].name,
                               gx   = flow_rate_kgPs,
                               type = 'COM1')
dat.add_generator(gen)


# #--- write TOUGH2 input file (obsolete)------------------------------------	
#dat.grid.blocklist.insert(0,dat.grid.blocklist[-1])
#del dat.grid.blocklist[-1]
#dat.grid.connectionlist.insert(0,dat.grid.connectionlist[-1])
#del dat.grid.connectionlist[-1]


# only run tough2 no toughreact
dat.add_react(mopr=[None,2,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

dat.write(dat.title)
