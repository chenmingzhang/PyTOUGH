import calc_swcc
import numpy as np
import matplotlib.pyplot as plt
import pdb
swcc={'slr'     : 0.045,
       'nv'     : 4.0,
       'pmax'   : 1.e8,
       'p0'     : 700,
       'sl_sat' : 1.,
       'pcap'   : None,
       'klr'    : None,
       'kgr'    : None
        }
# 
swcc_nv1=swcc.copy()
swcc_nv1['nv']  = 1.2

swcc_nv2=swcc.copy()
swcc_nv2['nv']  = 2.0

swcc_p1=swcc.copy()
swcc_p1['p0']  = 8000

swcc_p2=swcc.copy()
swcc_p2['p0']  = 1000
#slr      = 0.045
##nv       = 2.1
##nv       = 1.2
#nv       = 4.0
#pmax     = 1.e8
#p0       = 700  # unit
#sl_sat   = 1.

#pdb.set_trace()

sw=np.concatenate((np.linspace(0,swcc['slr'],100) ,    np.linspace(swcc['slr']+1.e-5,1,100)))

[swcc['pcap']    ,swcc['klr']    ,swcc['kgr']    ]  =  calc_swcc.swcc_van_genuchten_tough2(slr=swcc['slr']    ,sw_plot=False,p0=    swcc['p0']    ,nv=swcc['nv']    )
[swcc_nv1['pcap'],swcc_nv1['klr'],swcc_nv1['kgr']]  =  calc_swcc.swcc_van_genuchten_tough2(slr=swcc_nv1['slr'],sw_plot=False,p0=swcc_nv1['p0'],nv=swcc_nv1['nv'])
[swcc_nv2['pcap'],swcc_nv2['klr'],swcc_nv2['kgr']]  =  calc_swcc.swcc_van_genuchten_tough2(slr=swcc_nv2['slr'],sw_plot=False,p0=swcc_nv2['p0'],nv=swcc_nv2['nv'])


[swcc_p1['pcap'],swcc_p1['klr'],swcc_p1['kgr']]  =  calc_swcc.swcc_van_genuchten_tough2(slr=swcc_p1['slr'],sw_plot=False,p0=swcc_p1['p0'],nv=swcc_p1['nv'])
[swcc_p2['pcap'],swcc_p2['klr'],swcc_p2['kgr']]  =  calc_swcc.swcc_van_genuchten_tough2(slr=swcc_p2['slr'],sw_plot=False,p0=swcc_p2['p0'],nv=swcc_p2['nv'])




fig = plt.figure()
fig.subplots_adjust(hspace=0.5,wspace=0.5)
fig.subplots_adjust(left=0.17, right=0.93, top=0.93, bottom=0.15)
ax1  = fig.add_subplot(121)
plt.plot(sw,swcc['pcap'],'r.-'    ,label=str(swcc['nv'])    )
plt.plot(sw,swcc_nv1['pcap'],'g.-',label=str(swcc_nv1['nv']))
plt.plot(sw,swcc_nv2['pcap'],'b.-',label=str(swcc_nv2['nv']))



plt.legend()
plt.xlabel('SATURATION')
plt.ylabel('CAPILLARY PRESSURE (Pa)')
ax1.set_yscale('log')
plt.grid()
ax2  = fig.add_subplot(122)
ax2.plot(sw,swcc['klr'],'r-o',sw,swcc_nv1['klr'],'g-o',sw,swcc_nv2['klr'],'b-o')
ax2.set_yscale('log')
plt.xlabel('SATURATION')
plt.ylabel('RELATIVE PERMEABILITY')
plt.ylim(1e-16,1)
plt.grid()
plt.savefig("figure/"+'compare_swcc_nv'+".png",dpi=300)



fig = plt.figure()
fig.subplots_adjust(hspace=0.5,wspace=0.5)
fig.subplots_adjust(left=0.17, right=0.93, top=0.93, bottom=0.15)
ax1  = fig.add_subplot(121)
#plt.plot(sw,swcc['pcap'],'r.-',sw,swcc_p1['pcap'],'g.-',sw,swcc_p2['pcap'])


plt.plot(sw,swcc['pcap']   ,'r.-',label=str(   swcc['p0'])    )
plt.plot(sw,swcc_p1['pcap'],'g.-',label=str(swcc_p1['p0']))
plt.plot(sw,swcc_p2['pcap'],'b.-',label=str(swcc_p2['p0']))
plt.legend()
plt.xlabel('SATURATION')
plt.ylabel('CAPILLARY PRESSURE (Pa)')
ax1.set_yscale('log')
plt.grid()
ax2  = fig.add_subplot(122)
ax2.plot(sw,swcc['klr'],'r-o',sw,swcc_p1['klr'],'g-o',sw,swcc_p2['klr'],'b-o')
ax2.set_yscale('log')
plt.xlabel('SATURATION')
plt.ylabel('RELATIVE PERMEABILITY')
plt.ylim(1e-16,1)
plt.grid()
plt.savefig("figure/"+'compare_swcc_p0'+".png",dpi=300)




