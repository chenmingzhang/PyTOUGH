import numpy as np
from t2listing import *
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
sPday                  = 3600*24.
T_init_c               = 10.0
p_atm_pa               = 101.3e3
simulation_time_s      = 1000*86400*10
max_no_time_steps      = 9999 
dayPyear               = 365.25
mmass_sulphate_kgPmol  = 0.096   #so4-2
mgPkg                  = 1.e6
mmass_iron2_kgPmol     = 0.056
mmass_mg_kgPmol     = 0.024
mmass_ca_kgPmol     = 0.040
mmass_hco3_kgPmol   = 0.061
mmass_o2_kgPmol   = 0.032



inp       = t2data()
inp.title = 'flow.inp'


# delete exisiting input file
cwd=os.getcwd()
inp_path=os.path.join(os.getcwd(),inp.title)

directory_name = os.path.basename(cwd)







# ---- set up the model ---------------------------------
length = 4  #400.
#length = 400  #400.
nblks  = 15
dz     = [length / nblks] * nblks
dy     = dx  = [0.1]
geo    = mulgrid().rectangular(dx, dy, dz)
#geo   = mulgrid().rectangular(dx, dy, dz, atmos_type = 0)
#geo.write(inp.title+'.dat')

print("Total cell number is " + str(nblks) +"\n")

# #Create TOUGH2 input data file:
inp.grid = t2grid().fromgeo(geo)
inp.parameter.update(
    {'max_timesteps'  : max_no_time_steps,     # maximum number of time steps, 9999 in TR means max_timesteps do not restrict the simulation time
     'const_timestep' : -1,
     'tstop'          : simulation_time_s,
     'gravity'        : 9.81,
     'print_level'    : 2,      #-3 SO far TR can not handle print level >2
     'texp'           : 2.41e-05,   # default vapour diffusion coefficient. note this is not 1e-9m2/s for solute
     'timestep'       : [0.0001],
     'be'             : 2.334,
     'default_incons' : [p_atm_pa, 10.99, T_init_c, None],
     'relative_error' : 1.e-6,
     'print_interval' : max_no_time_steps/20,
     'max_timestep'   : 8640*500  # 0  #h*5 #8640*0.001   #8640*5  # 8640*0.01 seems working  #8640*0.05 #5000 #50000   #86400     # the maximum length of time step in second
     })
	 
#inp.parameter['max_timestep']   = inp.parameter['tstop']/inp.parameter['max_timesteps']

inp.start = True
inp.diffusion=[[2.13e-5,     0.e-8],   
               [2.13e-5,     0.e-8]]
inp.multi={ 'num_components'           : 2,   # warning, the key needs to be exactly the same, no extra spacings
            'num_equations'            : 3,
            'num_phases'               : 2,
            'num_secondary_parameters' : 8}

# #Set MOPs:
inp.parameter['option'][1]  = 1       # mop(1) if unequal 0, a short printout for non-convergent iterations will be generated.
inp.parameter['option'][7]  = 1       # mop(7) if unequal 0, a printout of input data will be provided.
inp.parameter['option'][9]  = 1       # mop(9) determines the composition of produced fluid with the MASS option (see GENER, below). The relative amounts of phases are determined as follows: 1: produced source fluid has the same phase composition as the producing element
inp.parameter['option'][11] = 0       # mop(11)  = 0: MOBILITIES ARE UPSTREAM WEIGHTED WITH WUP. (DEFAULT IS WUP = 1.0). PERMEABILITY IS UPSTREAM WEIGHTED.
inp.parameter['option'][16] = 4       # mop(16) > 0: INCREASE TIME STEP BY AT LEAST A FACTOR 2, IF CONVERGENCE OCCURS IN .LE. MOP(16) ITERATIONS.
inp.parameter['option'][19] = 2       # 2 *** is used in some EOS-modules for selecting different options 
inp.parameter['option'][21] = 3       # 3: SUBROUTINE DSLUCS: BI-CONJUGATE GRADIENT SOLVER - LANCZOS TYPE; PRECONDITIONER: INCOMPLETE LU FACTORIZATION


# TIMES 
output_interval_days = 300    # output result for every 30 days.
inp.output_times = {'num_times_specified': int(simulation_time_s*dayPs/output_interval_days),
                    'time': list( np.arange(int(simulation_time_s*dayPs)) *sPday*output_interval_days   )}


# #Add another rocktype, with relative permeability and capillarity functions & parameters:

r1 = rocktype('SAND ', 
        nad           = 2,
        porosity      = 0.45,
        density       = 2650.,
        permeability  = [2.e-10, 2.e-10, 2.e-10],
        conductivity  = 2.51,
        specific_heat = 920)



#slr      = 0.045
##nv       = 2.1
##nv       = 1.2
#nv       = 4.0
#pmax     = 1.e8
#p_air_pa = 700  # unit
#sl_sat   = 1.

slr      = 0.045
#nv       = 2.1
#nv       = 1.2
nv       = 4.0
pmax     = 1.e8
#p_air_pa = 700  # unit
p_air_pa = 8000  # unit
sl_sat   = 1.

#nv=3.0
#nv=1.5
#nv=5
#p_air_pa= 500  # unit

#p_air_pa= 2000  # unit bad
#p_air_pa= 1000  # unit
#p_air_pa= 100  # unit ok but steep


inv_p0 = 1/p_air_pa
lam    = 1-1/nv

r1.capillarity           = {'type': 7, 'parameters': [lam, slr, inv_p0, pmax, sl_sat]}
r1.relative_permeability = {'type': 7, 'parameters': [lam, slr, 1. , 0.054]}
#r1.capillarity           = {'type': 7, 'parameters': [lam, slr-1.e-5, 1/p_air_pa, 1.e8, 1.]}
inp.grid.add_rocktype(r1)
	
r2 = rocktype('BOUND',
        nad           = 2,
        porosity      = 0.99,
        density       = 2650.,
        permeability  = [1.e-11, 1.e-11, 1.e-11],
        conductivity  = 2.51,
        specific_heat = 1.e5)
#r2.capillarity           = {'type': 7, 'parameters': [lam, slr, inv_p0, pmax, sl_sat]}
#r2.relative_permeability = {'type': 7, 'parameters': [lam, slr, 1. , 0.054]}
#r2.capillarity           = {'type': 1, 'parameters': [0. , 0., 1.0,sl_sat ]}    # should cp(1) be the  atmospheric pressure or zero?
r2.capillarity           = {'type': 1, 'parameters': [0 , 0., 1.0,sl_sat ]}    # should cp(1) be the  atmospheric pressure or zero?
r2.relative_permeability = {'type': 1, 'parameters': [0.1,0.0, 1.0,0.1,]}   #linear function for liquid water, rp(1)<sl<rp(3)  kl increaes from 0 to 1 ,  for gas, rp(2)<sg<rp(4) kg increase from 0 to 1
inp.grid.add_rocktype(r2)


bvol    = 1.e50
conarea = dx[0] * dy[0]
condist = 1.e-10      # distance between the large cell and 
  
# #assign rocktype and parameter values:
for blk in inp.grid.blocklist:
    blk.rocktype = r1
    blk.ahtx     = conarea   # interface area for heat exchange
	

# -------add boundary condition block on the surface-----------------
bdy01 = t2block('bdy01', bvol, r2,
             ahtx      = conarea, # area for heat exchange
             centre    = np.array([ dx[0]/2,dy[0]/2,0   ])   # important for plotting
             ) 

inp.grid.blocklist.insert(0,bdy01)

con1 = t2connection([inp.grid.block['  a 1'] , bdy01],
                    #distance  = [condist , 0.5*dz[0]],
                    distance  = [0.5*dz[0]   , condist  ],
                    area      = conarea, 
                    direction = 3,   # which to read permeability
                    dircos    = -1)  # ISOT not BETX

inp.grid.connectionlist.insert(0,con1)



	
# -----------add boundary condition block at the bottom --------------------------

bdy02 = t2block('bdy02', bvol, r2,
             ahtx      = conarea, # area for heat exchange
             centre    = np.array([ dx[0]/2, dy[0]/2, -4.1   ])   # important for plotting
             ) 

inp.grid.blocklist.insert( len(inp.grid.block)+1 ,bdy02)      #lenlen(inp.grid.block)+1 puts the element to the end

con2 = t2connection([bdy02,inp.grid.block['  a15']  ],
                    distance  = [condist , 0.5*dz[0]],
                    #distance  = [0.5*dz[0],condist],
                    area      = conarea, 
                    direction = 3,   # which to read permeability in blocks rocktype
                    dircos    = -1)  # ISOT not BETX

inp.grid.connectionlist.insert( len(inp.grid.connection)+1   ,con2)



# ----------- add initial condition --------------------------------------------
sg_init=0.0000001
for num,key in enumerate(inp.grid.blocklist):
    if str(key)[:3]=='  a':
        inp.incon[str(key)] = \
                [None, [p_atm_pa , 10.0+sg_init, T_init_c]]
                #[None, [p_atm_pa , 10.0001, T_init_c]]
                #[None, [p_atm_pa - inp.grid.block[str(key)].centre[2]*liquid_density_kgPm3*inp.parameter['gravity'], 10.01, T_init_c]]

#inp.incon['bdy01'] = [None, [p_atm_pa, 10.999, T_init_c]]    # initial condition on the surface . what does 0.999 mean?, meaning air saturation on the top is 0.99 , water saturation is 0.01
inp.incon['bdy01'] = [None, [p_atm_pa, 10.9999, T_init_c]]    # initial condition on the surface . what does 0.999 mean?, meaning air saturation on the top is 0.99 , water saturation is 0.01
inp.incon['bdy02'] = [None, [p_atm_pa, 10.0001, T_init_c]]   #  initial condition at the bottom what does 0.0001 mean? meaning air satuation at the bottom is 0.01%, liquid is 99.99%

# #add generator:
#recharge_rate_mmPday = 5.47 #1e-30 #5.47   # 2000mm /  365  days = 5.47mm/day mm1e-30
recharge_rate_mmPday = 5.47   # 2000mm /  365  days = 5.47mm/day mm1e-30
recharge_rate_kgPs   = recharge_rate_mmPday*conarea*liquid_density_kgPm3*mPmm*dayPs
gen              = t2generator(name  = 'INF 1', 
                               block = '  a 1',      #inp.grid.blocklist[0].name,
                               gx   = recharge_rate_kgPs,
                               type = 'COM1')
inp.add_generator(gen)

print("Recharge rate is " + str(recharge_rate_mmPday) +" mm/day\n")

# only run tough2 no toughreact
inp.add_react(mopr=[None,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1])

inp.write(inp.title)
print("file " + inp.title +" generated\n")

