#from t2listing import *   # post processing
#from t2data import *      # pre processing
import py_compile
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import importlib


pytough_path=os.environ['pytough']
print(os.environ['pytough'])

current_path=os.getcwd()

sys.path.append(os.path.join(pytough_path,'python'))

py_compile.compile(os.path.join(pytough_path,'python','t2listing.py'))
py_compile.compile(os.path.join(pytough_path,'python','t2data.py'))

import t2listing
import t2data
importlib.reload(t2listing)
importlib.reload(t2data)
import tr2data
importlib.reload(tr2data)

saturation=np.linspace(0,1,100)
cinp  = tr2data.t2data('chemical.inp')
#name = 'flow.inp'
inp  = t2data.t2data(name)

# print (inp.grid.rocktype)

# inp.parameter   # list all the control parameters

# rock_type=[i for i in inp.grid.rocktype]


# density=np.array([j.density for j in inp.grid.rocktypelist])
# porosity=np.array([j.porosity for j in inp.grid.rocktypelist])

# tortuosity=np.array([j.tortuosity for j in inp.grid.rocktypelist])
# compressibility=np.array([j.compressibility for j in inp.grid.rocktypelist])
# #see page 69 of pytough user t2block object
# #
element_coordinate_m=np.array([j.centre for j in inp.grid.blocklist])

### way to get the x and y as matrix
Amic_aqureshape_format=[11,7]
element_coordinate_m=np.array([j.centre for j in inp.grid.blocklist])
x_ay_all=np.array([i[0] for i in element_coordinate_m[1:]] )
x_mtx=x_ay_all.reshape(Amic_aqureshape_format)
y_ay_all=np.array([i[1] for i in element_coordinate_m[1:]] )
y_mtx=y_ay_all.reshape(Amic_aqureshape_format)
z_ay_all=np.array([i[2] for i in element_coordinate_m[1:]] )
z_mtx=z_ay_all.reshape(Amic_aqureshape_format)
# x_mtx here is the centre of each element


# obtaining dx dy and dz from coordinate.
x_ay=x_mtx[0]
y_ay=[i[0] for i in   y_mtx]
dy=[-2]*11
dz=[10]









# TO200324 the attempt to export from inp to vtz is failed because:
#1. the current grid is not regular given the first cell 'TOP 0'
## connects to the first row
#2. it requires geo file 'dat.grid = t2grid().fromgeo(geo)' wile geo
# is not available.



# #element_coordinate_m[1:,0]

# volume=np.array([j.volume for j in inp.grid.blocklist])
# rock_type=np.array([j.rocktype for j in inp.grid.blocklist])

# volume[1:].reshape(reshape_format)  # first is removed because

# rock_type[1:].reshape(reshape_format)
# array([[FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACT, MATRX, MATRX, MATRX, MATRX, MATRX, MATRX],
#        [FRACB, MATRB, MATRB, MATRB, MATRB, MATRB, MATRB]], dtype=object)



# num_connections=np.array([j.num_connections for j in inp.grid.blocklist])
# num_connections[1:].reshape(reshape_format)
# # array([[3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [3, 4, 4, 4, 4, 4, 3],
# #        [1, 1, 1, 1, 1, 1, 1]])

name=np.array([j.name for j in inp.grid.blocklist])
name_mtx=name[1:].reshape(Amic_aqureshape_format)
# # array([['    1', '2   1', '3   1', '4   1', '5   1', '6   1', '7   1'],
# #        ['    2', '2   2', '3   2', '4   2', '5   2', '6   2', '7   2'],
# #        ['    3', '2   3', '3   3', '4   3', '5   3', '6   3', '7   3'],
# #        ['    4', '2   4', '3   4', '4   4', '5   4', '6   4', '7   4'],
# #        ['    5', '2   5', '3   5', '4   5', '5   5', '6   5', '7   5'],
# #        ['    6', '2   6', '3   6', '4   6', '5   6', '6   6', '7   6'],
# #        ['    7', '2   7', '3   7', '4   7', '5   7', '6   7', '7   7'],
# #        ['    8', '2   8', '3   8', '4   8', '5   8', '6   8', '7   8'],
# #        ['    9', '2   9', '3   9', '4   9', '5   9', '6   9', '7   9'],
# #        ['   10', '2  10', '3  10', '4  10', '5  10', '6  10', '7  10'],
# #        ['wta 1', 'wta 2', 'wta 3', 'wta 4', 'wta 5', 'wta 6', 'wta 7']],
# #       dtype='<U5')

# neighbour_name=np.array([j.neighbour_name for j in inp.grid.blocklist])
# neighbour_name[1:].reshape(reshape_format)


# ahtx=np.array([j.ahtx for j in inp.grid.blocklist])
# ahtx[1:].reshape(reshape_format)


# num_connections=np.array([j.permeability for j in inp.grid.connectionlist])

# area=np.array([j.area for j in inp.grid.connectionlist])
# dircos=np.array([j.dircos for j in inp.grid.connectionlist])
# distance=np.array([j.distance for j in inp.grid.connectionlist])




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


# this is failed, because this is not in tecplot format
# Time evolution at specified elements
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

#opt.history(('e','TOP 0','PCAP'))   # THIS IS WORKING!!!


#Amic_aqu.history(('e','TOP 0','Sg')   )

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




##   TO200324 one way to figure out connection
## it is not possible to get mullgrid from input file because information is 
## insurfficient https://github.com/acroucher/PyTOUGH/issues/21
#mask_vertical_flow_direction=[not(i.dircos) for i in inp.grid.connectionlist]
# name_mtx[:-1,0]
# name_mtx[1:,0]
first_column_tuple=list(zip(name_mtx[:-1,0],name_mtx[1:,0]))
#connection_ay=opt.connection.DataFrame.row
#opt.connectionlist.DataFrame.row
#indices = np.where(np.in1d(first_column_tuple, opt.connection.DataFrame.row))[0]
#indx = [items.index(tupl) for tupl in items if tupl[0] == s]
#indx = [items.index(tupl) for tupl in items if tupl[0] == s]
#Output = [i for i, item in   enumerate(opt.connection.DataFrame.row)    if item == first_column_tuple[0] ]  #working  
mask_first_column_index_ay =  [  [i for i, item in   enumerate(opt.connection.DataFrame.row)    if item == j ] for j in   first_column_tuple   ]
mask_first_column_index_ay=np.array([i[0] for i in mask_first_column_index_ay])  # for flow output






