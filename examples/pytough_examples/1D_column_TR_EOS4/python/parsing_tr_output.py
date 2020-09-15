#from t2listing import *   # post processing
#from t2data import *      # pre processing
import py_compile
import sys
import os
import numpy as np
import matplotlib.pyplot as plt
import importlib
#def parsing_result ():


import t2listing
import t2data
importlib.reload(t2listing)
importlib.reload(t2data)

#saturation=np.linspace(0,1,100)

#name = 'flow.inp'
#inp  = t2data.t2data(name)

import tr2data
importlib.reload(tr2data)


print('Start parsing TOUGHREACT output file\n')
#
chem_inp  = tr2data.tr2data('chemical.inp')
#chem_inp.prim
#chem_inp.water
#

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
#Amic_aqureshape_format=[11,7]
#element_coordinate_m=np.array([j.centre for j in inp.grid.blocklist])
#x_ay_all=np.array([i[0] for i in element_coordinate_m[1:]] )
#x_mtx=x_ay_all.reshape(Amic_aqureshape_format)
#y_ay_all=np.array([i[1] for i in element_coordinate_m[1:]] )
#y_mtx=y_ay_all.reshape(Amic_aqureshape_format)
#z_ay_all=np.array([i[2] for i in element_coordinate_m[1:]] )
#z_mtx=z_ay_all.reshape(Amic_aqureshape_format)
## x_mtx here is the centre of each element
#
#
## obtaining dx dy and dz from coordinate.
#x_ay=x_mtx[0]
#y_ay=[i[0] for i in   y_mtx]
#dy=[-2]*11
#dz=[10]
#





# TO200324 the attempt to export from inp to vtz is failed because:
#1. the current grid is not regular given the first cell 'TOP 0'
## connects to the first row
#2. it requires geo file 'dat.grid = t2grid().fromgeo(geo)' wile geo
# is not available.



# #element_coordinate_m[1:,0]

volume    = np.array([j.volume for j in inp.grid.blocklist])
rock_type = np.array([j.rocktype for j in inp.grid.blocklist])

# volume[1:].reshape(reshape_format)  # first is removed because

#rock_type
#array([TUBES, TUBES, TUBES, TUBES, TUBES, TUBES, TUBES, TUBES, TUBES,
#       TUBES, TUBES, TUBES, TUBES, TUBES, TUBES, TUBES], dtype=object)


#num_connections
#Out[18]: array([1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
#WARNING: 1. THIS MEANS TOUGHREACT HAS YET IMPLIMENT THE FUCTION OF SUSSESSIVE 
#  CONNECTION MADE BY VARIABLE NESQ!
#WARNING: 2. THE X in input is only for plotting purpose and has nothing to do with the result



blk_name = np.array([j.name for j in inp.grid.blocklist])
#name
#Out[19]: 
#array(['F   1', 'F   2', 'F   3', 'F   4', 'F   5', 'F   6', 'F   7',
#       'F   8', 'F   9', 'F  10', 'F  11', 'F  12', 'F  13', 'F  14',
#       'F  15', 'F  16'], dtype='<U5')

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

print('Start parsing aqu file...\n')
aqu=t2listing.toughreact_tecplot('aqu.dat',inp.grid.blocklist)
#cc=Amic_aqu.history((inp.grid.block['TOP 0'],'Sg'))
#cc=Amic_aqu.history([(inp.grid.block['TOP 0'],'Sg'),    (inp.grid.block['    1'],'Sg')])

# both of them working.
#Amic_aqu.element.get_DataFrame
#Amic_aqu.element.DataFrame

# below are successful
print('Start parsing sod file...\n')
sod = t2listing.toughreact_tecplot('sod.dat',inp.grid.blocklist)
print('Start parsing gas file...\n')
gas   = t2listing.toughreact_tecplot('gas.dat',inp.grid.blocklist)


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

print('Start parsing flow.out...\n')
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
#first_column_tuple=list(zip(name_mtx[:-1,0],name_mtx[1:,0]))
#connection_ay=opt.connection.DataFrame.row
#opt.connectionlist.DataFrame.row
#indices = np.where(np.in1d(first_column_tuple, opt.connection.DataFrame.row))[0]
#indx = [items.index(tupl) for tupl in items if tupl[0] == s]
#indx = [items.index(tupl) for tupl in items if tupl[0] == s]
#Output = [i for i, item in   enumerate(opt.connection.DataFrame.row)    if item == first_column_tuple[0] ]  #working  
#mask_first_column_index_ay =  [  [i for i, item in   enumerate(opt.connection.DataFrame.row)    if item == j ] for j in   first_column_tuple   ]
#mask_first_column_index_ay=np.array([i[0] for i in mask_first_column_index_ay])  # for flow output



### create tx_mtx files for all the output for easy analysis
opt.first(); gas.first(); sod.first(); aqu.first()
plot_every=5
array_length=len(volume)

opt_idx= np.linspace(0,opt.num_times-1,6,dtype=int) 

# opt element matrix
opt.tx_ele_mtx={}
for j in opt.element.column_name:
    opt.tx_ele_mtx[j] =np.empty((0,array_length), float) 
for i in opt.times:
    for j in opt.element.column_name:
        opt.tx_ele_mtx[j] =  np.append(opt.tx_ele_mtx[j] , np.array([opt.element.DataFrame[j]]), axis=0)
    opt.next()

# opt connection matrix
opt.tx_con_mtx={}
opt.first();
for j in opt.connection.column_name:
    opt.tx_con_mtx[j] =np.empty((0,array_length-1), float) 
for i in opt.times:
    for j in opt.connection.column_name:
        opt.tx_con_mtx[j] =  np.append(opt.tx_con_mtx[j] , np.array([opt.connection.DataFrame[j]]), axis=0)
    opt.next()


# aquifer condition time x axis matrix  (useful when drawing contours)
aqu.first()
aqu.tx_mtx={}
for j in aqu.element.column_name:
    aqu.tx_mtx[j] =np.empty((0,array_length), float) 

for i in aqu.times:
    for j in aqu.element.column_name:
        aqu.tx_mtx[j] =  np.append(aqu.tx_mtx[j] , np.array([aqu.element.DataFrame[j]]), axis=0)
    aqu.next()
    

# aquifer mineral time x axis matrix
sod.tx_mtx={}
for j in sod.element.column_name:
    sod.tx_mtx[j] =np.empty((0,array_length), float) 
for i in sod.times:
    for j in sod.element.column_name:
        if '\x00' not in j:
            sod.tx_mtx[j] =  np.append(sod.tx_mtx[j] , np.array([sod.element.DataFrame[j]]), axis=0)
    sod.next()

# aquifer gas time x axis matrix
gas.tx_mtx={}
for j in gas.element.column_name:
    gas.tx_mtx[j] =np.empty((0,array_length), float) 
for i in gas.times:
    for j in gas.element.column_name:
        gas.tx_mtx[j] =  np.append(gas.tx_mtx[j] , np.array([gas.element.DataFrame[j]]), axis=0)
    gas.next()


#connection_x_location= np.vstack([sod.tx_mtx['X'][0][1:], sod.tx_mtx['X'][0][:-1]]).mean(axis=0)
con_depth_m= -np.vstack([sod.tx_mtx['Z'][0][1:], sod.tx_mtx['Z'][0][:-1]]).mean(axis=0)




