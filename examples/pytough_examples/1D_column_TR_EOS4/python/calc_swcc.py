# this script validate the swcc curve
import numpy as np
import matplotlib.pyplot as plt



##dat=inp
#
#capillarity_parameter           = dat.grid.rocktype['SAND '].capillarity['parameters']
#capillarity_type                = dat.grid.rocktype['SAND '].capillarity['type']
#relative_permeability_parameter = dat.grid.rocktype['SAND '].relative_permeability['parameters']
#relative_permeability_type      = dat.grid.rocktype['SAND '].relative_permeability['type']
#
##capillary parameter
##[0.23, 0.045, 0.001428, 100000000.0, 1.0]
##nv=1.3
#
#
#
#
#lam                       = capillarity_parameter[0]
#nv=  1/(1-lam)
#
#slr  = capillarity_parameter[1]
#
#p_zero_point                = 1./capillarity_parameter[2]
#
#pmax                = capillarity_parameter[3]
#
#sl_sat = capillarity_parameter[4]
#
#
#lam                       = capillarity_parameter[0]
#nv=  1/(1-lam)
#
#slr  = capillarity_parameter[1]
#
#p_zero_point                = 1./capillarity_parameter[2]
#
#pmax                = capillarity_parameter[3]
#
#sl_sat = capillarity_parameter[4]
#
#
#
#
#
#
#
##P_zero                      = np.linspace(P_zero_point-1500,P_zero_point+1500,5)     # what is p_zero
#
#
#
#
##saturation1 = np.linspace(slr,sl_sat,100)
#saturation1  = np.linspace(slr+1.e-5,1,100)     # sat from residue to 1
##saturation2 = np.linspace(0,slr,100)
#saturation2  = np.linspace(0,slr,50)            # sat from 0 to residue
#
#
#a=np.arange(10)
#

def swcc_van_genuchten_tough2(sat=None,lam=0.23,slr=0.045,inv_p0= 0.00142857,pmax=1e8,sl_sat=1,sw_plot=True,p0=None,nv=None):
    '''
    calculate capillary pressure based on the input soil water retention curve
    '''

    if sat==None:
        sat=np.concatenate((np.linspace(0,slr,100) ,    np.linspace(slr+1.e-5,sl_sat,100)))
    if p0!=None:
        inv_p0=1/p0
    if nv!=None:
        lam=1-1/nv

    nv=  1/(1-lam)
    p_zero_point    = 1./inv_p0
    

    p_cap = np.zeros(len(sat))


    mask_sat_gt_slr = sat>slr

    saturation1     = sat[mask_sat_gt_slr]
    saturation2     = sat[~mask_sat_gt_slr]

    s_star              = (saturation1-slr)/(sl_sat-slr)
    
    capillary_pressure1 = p_zero_point*(s_star**(-1/lam)-1)**(1-lam) 
    
    
    
    sbar                = 1.e-5/(sl_sat-slr)
    pce                 = p_zero_point*(sbar**(-1/lam)-1)**(1-lam)
    envg                = 1./(1-lam)
    pcslope             = -p_zero_point/lam/envg/(sl_sat-slr)*(sbar**(-1/lam)-1)**((1-envg)/envg)*sbar**(-(1+lam)/lam) 
    capillary_pressure2 = pce+pcslope*(saturation2-slr-1.e-5)
    
    
    if sw_plot:
    
        fig = plt.figure()
        ax  = fig.add_subplot(111)
        plt.plot(saturation1,capillary_pressure1,'r.-',saturation2,capillary_pressure2,'.-')
        #plt.plot(sl_xt_mtx[:,-1],     -pcap_xt_mtx_pa[:,-1],'b.-')
        
        plt.text(0.2, 10.e4*10**(2/1.5),'P_zero='+str(p_zero_point))
        plt.xlabel('saturation')
        plt.ylabel('capillary_pressure')
        #plt.ylim(10,1.e10)
        #plt.xlim(-0.1,1.1)
        #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        ax.set_yscale('log')
        plt.suptitle('lam = %5.2f , nv = %5.2f , slr= %5.3f \n, inv_p0 = %5.2e, p0 = %5.2e \npmax = %5.2e,  ' %(lam,nv,slr,inv_p0,p_zero_point,pmax ),fontsize=8)
    
    
    plt.savefig("figure/Capillary_&_SWCC_for_"+".png",dpi=300)


