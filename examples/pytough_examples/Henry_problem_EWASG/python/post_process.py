from t2listing import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from t2data import *
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

if not os.path.exists('figure'):
        os.makedirs('figure')

x1               = np.arange(min(element_value_x),length_x+length_x/nblks_x,length_x/nblks_x)
z1               = -1*np.arange(-1*max(element_value_z),length_z+length_z/nblks_z,length_z/nblks_z)
xi,zi            = np.meshgrid(x1,z1)
j=0
while j<4:
    i=10*2+j*10
    while i<nblks_x+1:
        xi[j,i]=np.nan
        zi[j,i]=np.nan
        i+=1
    j+=1
x1_flux          = np.arange(min(element_value_x)+length_x/nblks_x*0.5,length_x,length_x/nblks_x)
z1_flux          = -1*np.arange(-1*max(element_value_z)+length_z/nblks_z/2,length_z,length_z/nblks_z)
xi_flux,zi_flux  = np.meshgrid(x1_flux,z1_flux)

i=0
while i<lst.num_times:
    # fig=plt.figure(figsize=(14,20))
    # fig.subplots_adjust(hspace=.30,wspace=.2)
    # fig.subplots_adjust(left=0.07, right=0.93, top=0.93, bottom=0.05)
    fig=plt.figure()
    # salt_mass_fraction_in_liquid_grid=griddata((element_value_x,element_value_z),
	                                    # salt_mass_fraction_in_liquid[:,i],(xi,zi),method='linear')
    # liquid_flow_mmPday_x_grid=griddata((element_value_x[:-nblks_z],element_value_z[:-nblks_z]),
	                                    # liquid_flow_mmPday_x[:,i],(xi_flux,zi_flux),method='linear')	
    # liquid_flow_mmPday_z_grid=griddata((element_value_x[20:-nblks_x],element_value_z[20:-nblks_x]),
	                                    # liquid_flow_mmPday_z[:,i],(xi_flux,zi_flux),method='linear')										
    # level_1=np.linspace(0,0.3,11)
    # ax1 = plt.subplot(311)
    # cs2 = plt.contourf(x1, z1, salt_mass_fraction_in_liquid_grid, level_1, cmap=plt.cm.jet)
    # fig.colorbar(cs2, orientation='vertical',fraction=0.02,pad=0.05)
    # cs1 = plt.quiver(xi_flux,zi_flux,liquid_flow_mmPday_x_grid,liquid_flow_mmPday_z_grid,
                    	# pivot='mid', width=0.002,scale=1/0.0005, color='k')
    # qk = plt.quiverkey(cs1, 0.90, 1.1, 100, r'$100 \frac{mm}{day}$', labelpos='W',
                    	# fontproperties={'weight': 'light','size': 'small'})
    # plt.ylabel('y (m)')
    # plt.xlabel('x (m) salt_mass_fraction_in_liquid')
    # plt.ylim(-length_z,0)
    # plt.xlim(0,length_x)

    salt_mass_fraction_in_liquid_grid=griddata((element_value_x,element_value_z),
	                                            salt_mass_fraction_in_liquid[:,i],(xi,zi),method='linear')
    level_1=np.linspace(0,0.3,11)
    ax1 = plt.subplot(312)
    plt.plot(element_value_x,element_value_z,'k.')
    cs2 = plt.contourf(xi, zi, salt_mass_fraction_in_liquid_grid, level_1, cmap=plt.cm.jet)
    fig.colorbar(cs2, orientation='vertical',fraction=0.02,pad=0.05)
    plt.ylabel('y (m)')
    plt.xlabel('x (m) salt_mass_fraction_in_liquid')
    plt.ylim(-length_z,0)
    plt.xlim(0,length_x)


    liq_saturation_grid=griddata((element_value_x,element_value_z),liq_saturation[:,i],(xi,zi),method='linear')
    level_2=np.linspace(0,1.,11)
    ax2=plt.subplot(313)
    cs=plt.contourf(xi, zi, liq_saturation_grid, level_2, cmap=plt.cm.jet)
    fig.colorbar(cs, orientation='vertical',fraction=0.02,pad=0.05)
    plt.ylabel('y (m)')
    plt.xlabel('x (m) liq_saturation')
    plt.ylim(-length_z,0)
    plt.xlim(0,length_x)

    fig.suptitle('time: %6.2e s' %lst.times[i])
    plt.rcParams.update({'font.size':10})
    fig.tight_layout()
    plt.savefig('figure/output_'+str(i+101)+'.png',dpi=300) 
    i+=1

#plt.close('all')