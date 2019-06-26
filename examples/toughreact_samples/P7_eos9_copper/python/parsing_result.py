#from t2listing import *   # post processing
#from t2data import *      # pre processing
import py_compile
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

pytough_path=os.environ['pytough']
print(os.environ['pytough'])

current_path=os.getcwd()

sys.path.append(os.path.join(pytough_path,'python'))

py_compile.compile(os.path.join(pytough_path,'python','t2listing.py'))
py_compile.compile(os.path.join(pytough_path,'python','t2data.py'))

import t2listing
import t2data
reload(t2listing)
reload(t2data)

#saturation=np.linspace(0,1,100)

name = 'flow.inp'
inp  = t2data.t2data(name)

print inp.grid.rocktype

inp.parameter   # list all the control parameters

rock_type=[i for i in inp.grid.rocktype]




## this is to get result from toughreact tecplot results
#Amic_aqu=t2listing.toughreact_tecplot('Amic_aqu.dat',inp.grid.block)
# TO190624 how to check a change of a point over time? A: Amic_gas.times Amic_gas.time could do something. Amic_gas.num_times
# TO190624 Amic_gas.index the current result out of all the Amic_gas.num_times .
# Amic_gas.element.num_rows the same as inp.grid.block
# Amic_gas.element.column_name get all the names of the columns
#inp.grid.block is been considered as block file, what is exactly considered as 'geo' file?
# 
# from example of 3d in pytough, geom.dat has keyword VERTICES and GRID

Amic_aqu=t2listing.toughreact_tecplot('Amic_aqu.dat',inp.grid.blocklist)
#cc=Amic_aqu.history((inp.grid.block['TOP 0'],'Sg'))
#cc=Amic_aqu.history([(inp.grid.block['TOP 0'],'Sg'),    (inp.grid.block['    1'],'Sg')])

# both of them working.
#Amic_aqu.element.get_DataFrame
#Amic_aqu.element.DataFrame

# below are successful
Amic_sod=t2listing.toughreact_tecplot('Amic_sod.dat',inp.grid.blocklist)
Amic_gas=t2listing.toughreact_tecplot('Amic_gas.dat',inp.grid.blocklist)


# this is failed
#Amic_tim=t2listing.toughreact_tecplot('Amic_tim.dat',inp.grid.block)

#  Amic_aqu.element.get_DataFrame  

#porosity_DRIFT=inp.grid.rocktype['DRIFT'].porosity # porosity
#
#capillarity_parameter_array_DRIFT=inp.grid.rocktype['DRIFT'].capillarity['parameters']    # capillary parameters
#capillarity_type_DRIFT=inp.grid.rocktype['DRIFT'].capillarity['type']     # 
#
#relative_permeability_parameter_array_DRIFT=inp.grid.rocktype['DRIFT'].relative_permeability['parameters']
#
#relative_permeability_type_DRIFT=inp.grid.rocktype['DRIFT'].relative_permeability['type']

#fig=plt.figure()
#ax3=plt.subplot(211)

name_output='flow.out'
opt=t2listing.t2listing(name_output)

#opt.history([(inp.grid.block['TOP 0'],'Sg'),    (inp.grid.block['    1'],'Sg')]) #not working

#opt.history(('e',inp.grid.block['TOP 0'],'PCAP'))  # not working

opt.history(('e','TOP 0','PCAP'))   # THIS IS WORKING!!!


# the S(liq) in 'flow.out' is the same as 'Amic_aqu.dat'

#inp.grid.blocklist[2].centre  # this is to check the xyz location 

## below not successful
#name_output='chemical.out'
#chem_opt=t2listing.t2listing(name_output)


### below not successful
#solute_inp_name='solute.inp' # seems not working
#solute_inp = t2data.t2data(solute_inp_name)


### below not succesful
#solute_opt_name='solute.out'
#solute_opt=t2listing.t2listing(solute_opt_name)

#
element_coordinate_m=np.array([j.centre for j in inp.grid.blocklist])



##fig = plt.figure()
##ax = fig.add_subplot(111, projection='3d')
##ax.scatter(element_coordinate_m[:,0], element_coordinate_m[:,1], element_coordinate_m[:,2], s=60, c='r', marker='s')
###ax.scatter(element_coordinate_m[0,0], element_coordinate_m[0,1], element_coordinate_m[0,2], s=10, c='b', marker='v')
###ax.scatter(element_coordinate_m[-1,0], element_coordinate_m[-1,1], element_coordinate_m[-1,2], s=10, c='b', marker='^')
##ax.set_xlabel('X Label')
##ax.set_ylabel('Y Label')
##ax.set_zlabel('Z Label')
##fig.suptitle('mesh_element')
##plt.rcParams.update({'font.size': 10})
###fig.tight_layout()
##plt.savefig("generated_mesh_grid.png",dpi=300) 
##



#chemical.inp is yet parsed.
#chemical.out is yet parsed.


#opt.last()

#opt.time
#opt.times # this is to list all the "tab" in the spreadsheet
#opt.simulator
#opt.element
#opt.element.DataFrame
#opt.element.row_name # the first colunm
#opt.connection.row_name 
#opt.connection.column_name
#opt.element.column_name







