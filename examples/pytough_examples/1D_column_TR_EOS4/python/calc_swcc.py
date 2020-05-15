# this script validate the swcc curve
import numpy as np
import matplotlib.pyplot as plt
import pdb



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

def swcc_van_genuchten_tough2(sat=None,lam=0.23,slr=0.045,inv_p0= 0.00142857,pmax=1e8,sl_sat=1,sw_plot=True,p0=None,nv=None,sgr=0.054):
    '''
    calculate capillary pressure based on the input soil water retention curve
    default values
    sat=None,lam=0.23,slr=0.045,inv_p0= 0.00142857,pmax=1e8,sl_sat=1,sw_plot=True,p0=None,nv=None
    a example to run the command

        a=calc_swcc.swcc_van_genuchten_tough2()

    '''

    if sat==None:
        sat=np.concatenate((np.linspace(0,slr,100) ,    np.linspace(slr+1.e-5,sl_sat,100)))
    if p0!=None:
        inv_p0=1/p0
    if nv!=None:
        lam=1-1/nv
    else:
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


    p_cap[mask_sat_gt_slr] = capillary_pressure1
    p_cap[~mask_sat_gt_slr] = capillary_pressure2

    #lam        = relative_permeability_parameter[0]
    #slr        = relative_permeability_parameter[1]
    #sl_sat     = relative_permeability_parameter[2]
    #sgr        = relative_permeability_parameter[3]
    
    #relative permeability is calcuated by subroutine relp in t2f_v2.f
    s_star                = (sat-slr)/(sl_sat-slr)
    mask_pos_s_star       = s_star>0
    klr                   = np.zeros(len(sat))
    klr[~mask_pos_s_star] = 0




    s_bar                = (sat-slr)/(1-sgr-slr)
    klr[mask_pos_s_star] = s_star[mask_pos_s_star]**0.5*(1-(1-s_star[mask_pos_s_star]**(1/lam))**lam)**2
    klr[sat >=   sl_sat] = 1
    kgr                  = (1-s_bar)**2*(1-s_bar**2)
    if sgr==0:
        kgr=1-klr
    

    
    
    #pdb.set_trace()
    if sw_plot:
    
        fig = plt.figure()
        fig.subplots_adjust(hspace=0.5,wspace=0.5)
        fig.subplots_adjust(left=0.17, right=0.93, top=0.93, bottom=0.15)
        ax1  = fig.add_subplot(121)
        plt.plot(saturation1,capillary_pressure1,'r.-',saturation2,capillary_pressure2,'.-')
        #plt.plot(sl_xt_mtx[:,-1],     -pcap_xt_mtx_pa[:,-1],'b.-')
        
        #plt.text(0.2, 10.e4*10**(2/1.5),'P_zero='+str(p_zero_point))
        plt.xlabel('SATURATION')
        plt.ylabel('CAPILLARY PRESSURE (Pa)')
        #plt.ylim(10,1.e10)
        #plt.xlim(-0.1,1.1)
        #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
        ax1.set_yscale('log')
        plt.grid()
        plt.suptitle('lam = %5.2f , nv = %5.2f , slr= %5.3f , inv_p0 = %5.2e, p0 = %5.2e pmax = %5.2e,  ' %(lam,nv,slr,inv_p0,p_zero_point,pmax ),fontsize=8)
        filename='SWCC_lam_%5.2f_nv_%5.2f_slr_%5.3f_invp0_%5.2e_p0_%5.2e_pmax_%5.2e,  ' %(lam,nv,slr,inv_p0,p_zero_point,pmax )
        filename=filename.replace('+','').replace('-','n').replace(' ','')
        ax2  = fig.add_subplot(122)
        ax2.plot(sat,klr,'k-o',)
        ax2.plot(sat,kgr,'r-o',)
        ax2.set_yscale('log')
        plt.xlabel('SATURATION')
        plt.ylabel('RELATIVE PERMEABILITY')
        plt.ylim(1e-16,1)
        plt.grid()
        plt.savefig("figure/"+filename+".png",dpi=300)


    return [p_cap,klr,kgr]


