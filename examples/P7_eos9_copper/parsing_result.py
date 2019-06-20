#from t2listing import *   # post processing
#from t2data import *      # pre processing
import py_compile
import sys
import os
import numpy as np

pytough_path=os.environ['pytough']
print(os.environ['pytough'])

current_path=os.getcwd()

sys.path.append(pytough_path)

py_compile.compile(os.path.join(pytough_path,'t2listing.py'))
py_compile.compile(os.path.join(pytough_path,'t2data.py'))

import t2listing
import t2data
reload(t2listing)
reload(t2data)

#saturation=np.linspace(0,1,100)

name = 'flow.inp'
dat  = t2data.t2data(name)

print dat.grid.rocktype

dat.parameter   # list all the control parameters

rock_type=[i for i in dat.grid.rocktype]



porosity_DRIFT=dat.grid.rocktype['DRIFT'].porosity # porosity

capillarity_parameter_array_DRIFT=dat.grid.rocktype['DRIFT'].capillarity['parameters']    # capillary parameters
capillarity_type_DRIFT=dat.grid.rocktype['DRIFT'].capillarity['type']     # 

relative_permeability_parameter_array_DRIFT=dat.grid.rocktype['DRIFT'].relative_permeability['parameters']

relative_permeability_type_DRIFT=dat.grid.rocktype['DRIFT'].relative_permeability['type']

#fig=plt.figure()
#ax3=plt.subplot(211)

name_output='flow.out'
opt=t2listing.t2listing(name)
