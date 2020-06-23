import numpy as np
import matplotlib
matplotlib.use('Agg')  # disabled all the jumping out figures
import matplotlib.pyplot as plt
import csv
import os
from t2listing import *
from t2data import *
from mpl_toolkits.mplot3d import Axes3D
# Turn interactive plotting off
#plt.ioff()

if not os.path.exists('figure'):
        os.makedirs('figure')


# delete existing png to avoid old png mixing with new ones
if os.path.exists('figure'):
    fig_path  = os.path.join(os.getcwd(),'figure')
    fig_files = os.listdir(fig_path)
    count=0
    for item in fig_files:
        if item.endswith(".png"):
            count+=1
            #os.remove(os.path.join( fig_path , item))
    #print("Existing "+ str(count)+ " png file" + " deleted\n")
else:
    print("figure directory does not exist and created.\n")
    os.makedirs('figure')


# plotting results
i=1
while i<lst.num_times:
    print("plotting " + str(i) + " / " + str(lst.num_times) + " result\n")

    #fig=plt.figure(figsize=(16,20))
    fig=plt.figure(figsize=(12,12))
    fig.subplots_adjust(hspace=.3,wspace=.2)
    #fig.subplots_adjust(left=0.07, right=0.93, top=0.93, bottom=0.05)
	
    ax3=plt.subplot(441)
    ax3.plot(t_xt_mtx[:,i],ele_depth_m  ,'r1-')
    plt.tick_params(
                axis='y',         
                which='both',    
                labelleft=True,
                labelright=False,
                right=True
                )
    plt.xlabel('Temperature \n(Celsius)')
    plt.ylabel('Depth (m)')
    #plt.ylim(-0.1,1.1)
    plt.xlim(20,30)
    plt.gca().invert_yaxis()
    plt.grid()

    #plt.xlim(np.min(temperature_degree),np.max(temperature_degree))
    #ax3.set_yscale('log')
    #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0)) 
    # ax3.spines['top'].set_color('red')
    # ax3.xaxis.label.set_color('red')
    # ax3.tick_params(axis='x', colors='red')

    ax1=plt.subplot(442)
    ax1.plot(p_xt_mtx_pa[:,i]*kpaPpa, ele_depth_m  [:],'k1-')
    plt.xlabel('Gas Pressure \n(Kpa)')
    #ax1.spines['top'].set_color('red')
    #plt.ylim(-0.1,1.1)
    plt.xlim(100,104)
    plt.xlim(np.min(p_xt_mtx_pa[:]*kpaPpa),np.max(p_xt_mtx_pa[:]*kpaPpa))
    plt.tick_params(
                axis='y',         
                which='both',    
                labelleft=False,
                labelright=False,
                right=True
                )
    #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    #ax1.set_yscale('log')
    ax2=ax1.twiny()
    ax2.plot(flo_gas_xt_mtx_mmPday[:,i],con_depth_m    ,'r1-')
    plt.xlabel('Gas Velocity \n(mm/day)')
    # plt.ylabel('high (m)')
    #plt.ylim(-0.1,1.1)
    #plt.xlim(100,115)
    plt.xlim(np.min(flo_gas_xt_mtx_mmPday),np.max(flo_gas_xt_mtx_mmPday))
    #ax2.set_yscale('log')
    #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    ax2.spines['top'].set_color('red')
    ax2.xaxis.label.set_color('red')
    ax2.tick_params(axis='x', 
            colors='red')	 
    plt.gca().invert_yaxis()
    plt.grid()





    ax3=plt.subplot(443)
    #ax3.plot(vap_dif_xt_mtx_mmPday[:,i],con_depth_m    ,'k1-')
    ax3.plot(flo_liq_xt_mtx_mmPday[:,i],con_depth_m    ,'k1-')
    ax3.plot(flo_gas_xt_mtx_mmPday[:,i],con_depth_m    ,'r1-')
    ax3.plot(vap_dif_xt_mtx_mmPday[:,i],con_depth_m    ,'b1-')
    #plt.xlabel('Vapor Diffusion \n(mm/day)')
    plt.xlabel('flow velocity \n(mm/day)')
    # plt.ylabel('high (m)')
    #plt.ylim(-0.1,1.1)
    #plt.xlim(-0.2,5)
    plt.tick_params(
                axis='y',         
                which='both',    
                labelleft=True,
                labelright=False,
                right=True
                )
    #plt.xlim(np.nanmin(vap_dif_mmPday)*1.e2,np.nanmax(vap_dif_mmPday)*1.e2)			
    #ax4=ax3.twiny()	
    #ax4.plot(flo_liq_xt_mtx_mmPday[:,i],con_depth_m    ,'r1-')
    plt.xlabel('Liquid Velocity \n(mm/day)')
    # plt.ylabel('high (m)')
    #plt.ylim(-0.1,1.1)
    #plt.xlim(-0.2,5)
    #plt.xlim(np.nanmin(flo_liq_mmPday)*100,np.nanmax(flo_liq_mmPday)*100)	
    #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    #ax4.spines['top'].set_color('red')	
    #ax4.xaxis.label.set_color('red')
    #ax4.tick_params(axis='x', colors='red')	 	
    #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))    
    plt.gca().invert_yaxis()
    plt.grid()

    ax3=plt.subplot(444)
    ax3.plot(sl_xt_mtx[:,i]*100,ele_depth_m  [:],'k1-')
    plt.xlabel('Liquid saturation \n(%)')
    # plt.ylabel('high (m)')
    #plt.ylim(-0.1,1.1)
    plt.xlim(-5,105)
    plt.tick_params(
                axis='y',         
                which='both',    
                labelleft=False,
                labelright=True,
                right=True
                )
    ax4=ax3.twiny()
    ax4.plot(-pcap_xt_mtx_pa[:,i]*kpaPpa,ele_depth_m  [:],'r1-')
    ax4.set_xscale('log')
    plt.xlabel('-Capillary Pressure \n(Kpa)')
    # plt.ylabel('high (m)')
    #plt.ylim(1.1,-0.1)
    #plt.xlim(-50,0.1)
    #plt.xlim(np.min(pcap_xt_mtx_pa[1:]*kpaPpa),np.max(pcap_xt_mtx_pa[1:]*kpaPpa))
    #ax3.set_yscale('log')
    #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
    ax4.spines['top'].set_color('red')	
    ax4.xaxis.label.set_color('red')
    ax4.tick_params(axis='x', colors='red')	 	
    #plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))    
    plt.gca().invert_yaxis()
    plt.grid()


    # change of value over time
    ax7=plt.subplot(713)
    ax7.plot(lst.times[:i]*dayPs,vap_dif_top_mmPday[:i]   ,'k1-',label='a1 to atm' )
    ax7.plot(lst.times[:i]*dayPs,vap_dif_second_mmPday[:i],'r1-',label='a2 to a1' )
    plt.ylabel('Vapor Diffusion\n(mm/day)')
    #plt.xlabel('Time (day)')
    #plt.ylim(0.08,0.13)
    #plt.ylim(np.min(vap_dif_top_mmPday),np.max(vap_dif_top_mmPday))
    plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.legend(loc="upper right",prop={'size':10})
    #ax7.set_xscale('log')
    #ax8 = ax7.twinx() 
    #plt.ylim(-1.3e-1,-6e-2)
    #plt.ylim(1.05*np.min(vap_adv_top_mmPday),1.05*np.max(vap_adv_top_mmPday))
    #plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #plt.ylabel('Vapor Adv.\na1 to atm\n (mm/day)')
    #plt.xlabel('Time (day)')
    #ax8.set_xscale('log')
    #ax8.spines['right'].set_color('red')
    #ax8.yaxis.label.set_color('red')
    #ax8.tick_params(axis='y', colors='red')
    plt.tick_params(
                axis='x',         
                which='both',    
                labelbottom=False,
                )
    plt.grid()
	
    ax7=plt.subplot(714)
    ax7.plot(lst.times[:i]*dayPs,flo_liq_top_mmPday[:i],'k1-',label='a1 to atm')
    ax7.plot(lst.times[:i]*dayPs,flo_liq_second_mmPday[:i],'r1-',label='a2 to a1')
    plt.ylabel('Liquid Vel.\n (mm/day)')
    #plt.xlabel('Time (day)')
    #plt.ylim(-0.1e-3,0.11e-2)
    #plt.ylim(np.min(flo_liq_second_mmPday),np.max(flo_liq_second_mmPday))
    plt.xlim(0,np.max(lst.times)*dayPs)
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.legend(loc="upper right",prop={'size':10})
    #ax7.set_xscale('log')
    #ax8 = ax7.twinx() 
    #ax8.plot(lst.times[:i]*dayPs,flo_liq_top_mmPday[:i],'r1-',)
    #plt.ylim(-1.e1,1.1e2)
    #plt.ylim(np.min(flo_liq_top_mmPday),np.max(flo_liq_top_mmPday))
    #plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #plt.ylabel('Liquid Velocity\na1 to atm\n (mm/day)')
    #plt.xlabel('Time (day)')
    #ax8.set_xscale('log')
    #ax8.spines['right'].set_color('red')
    #ax8.yaxis.label.set_color('red')
    #ax8.tick_params(axis='y', colors='red')		
    plt.tick_params(
                axis='x',         
                which='both',    
                labelbottom=False,
                )
    plt.grid()
	
    ax7=plt.subplot(715)
    #ax7.plot(lst.times[:i]*dayPs,vap_dif_second_mmPday[:i],'k1-')
    ax7.plot(lst.times[:i]*dayPs,vap_adv_top_mmPday[:i]   ,'k1-',label='a1 to atm')
    ax7.plot(lst.times[:i]*dayPs,vap_adv_second_mmPday[:i],'r1-',label='a2 to a1')
    plt.ylabel('Vapor Adv\n (mm/day)')
    #plt.xlabel('Time (day)')
    #plt.ylim(0.08,0.13)
    #plt.ylim(np.min(vap_dif_second_mmPday),np.max(vap_dif_second_mmPday))
    #plt.xlim(0,np.max(lst.times)*dayPs)
    # plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #ax7.set_xscale('log')
    #ax8 = ax7.twinx() 
    #ax8.plot(lst.times[:i]*dayPs,vap_adv_second_mmPday[:i],'r1-',)
    #plt.ylim(-1.3e-1,-6e-2)
    #plt.ylim(np.min(vap_adv_second_mmPday),np.max(vap_adv_second_mmPday))
    plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.legend(loc="right",prop={'size':10})
    #plt.ylabel('Vapor Adv\na2 to a1\n (mm/day)')
    #plt.xlabel('Time (day)')
    #ax8.set_xscale('log')
    #ax8.spines['right'].set_color('red')
    #ax8.yaxis.label.set_color('red')
    #ax8.tick_params(axis='y', colors='red')
    plt.tick_params(
                axis='x',         
                which='both',    
                labelbottom=False,
                )
    plt.grid()
	
    ax7=plt.subplot(716)
    ax7.plot(lst.times[:i]*dayPs,water_flow_top_mmPday[:i],'k1-',label='a1 to atm')
    ax7.plot(lst.times[:i]*dayPs,water_flow_second_mmPday[:i],'r1-',label='a2 to a1')
    plt.ylabel('Water Flux\n(mm/day)')
    #plt.xlabel('Time (day)')
    #plt.ylim(-0.1e-3,0.11e-2)
    #plt.ylim(np.min(water_flow_second_mmPday),np.max(water_flow_second_mmPday))
    plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #ax7.set_xscale('log')
    ax8 = ax7.twinx() 
    ax8.plot(lst.times[:i]*dayPs,cumsum_water_flow_second_mm[:i],'g1-',)
    #plt.ylim(-1.e1,1.1e2)
    #plt.ylim(np.min(cumsum_water_flow_second_mm),np.max(cumsum_water_flow_second_mm))
    plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.ylabel('Total water loss\na2 to a1\n (mm)')
    #plt.xlabel('Time (day)')
    #ax8.set_xscale('log')
    ax8.spines['right'].set_color('red')
    ax8.yaxis.label.set_color('red')
    ax8.tick_params(axis='y', colors='red')			
    plt.legend(loc="right",prop={'size':10})
    plt.tick_params(
                axis='x',         
                which='both',    
                labelbottom=False,
                )
    plt.grid()
	
    ax7=plt.subplot(717)
    ax7.plot(lst.times[:i]*dayPs,water_generation_vapor_mmPday[:,:i][0],'k1-')
    plt.ylabel('Vapor generation\n(mm/day)')
    plt.xlabel('Time (day)')
    #plt.ylim(-0.1e-3,0.11e-2)
    #plt.ylim(-5.5,0.5)
    plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    #ax7.set_xscale('log')
    ax8 = ax7.twinx() 
    ax8.plot(lst.times[:i]*dayPs,water_generation_liquid_mmPday[:,:i][0],'r1-',lst.times[:i]*dayPs,water_generation_mmPday[:,:i][0],'k1-')
    #plt.ylim(-1.e1,1.1e2)
    #plt.ylim(-5.5,0.5)
    plt.xlim(0,np.max(lst.times)*dayPs)
    #plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
    plt.ylabel('Liquid generation\n(mm/day)')
    #plt.xlabel('Time (day)')
    #ax8.set_xscale('log')
    ax8.spines['right'].set_color('red')
    ax8.yaxis.label.set_color('red')
    ax8.tick_params(axis='y', colors='red')			
    plt.grid()

    # ax7=plt.subplot(818)
    # ax7.plot(lst.times[:i]*dayPs,water_generation_mmPday[:,:i][0],'k1-')
    # plt.ylim(-6,-4)
    # plt.xlim(0,np.max(lst.times)*dayPs)
    # ax7.set_xscale('log')
    # #plt.ylabel('water generation\n(mm/day)')
    # plt.xlabel('Time (day)')
    # ax8 = ax7.twinx() 
    # ax8.plot(lst.times[:i]*dayPs,water_generation_mmPday[:,:i][0],'r1-',)
    # plt.ylabel('water generation\n(mm/day)')
    # plt.ylim(-6,-4)
    # plt.xlim(0,np.max(lst.times)*dayPs)
    # plt.xlabel('Time (day)')
    # ax8.set_xscale('log')
    # ax8.spines['right'].set_color('red')
    # ax8.yaxis.label.set_color('red')
    # ax8.tick_params(axis='y', colors='red')			

	
    fig.suptitle('time: %6.2e days' %(lst.times[i]*dayPs))
    plt.rcParams.update({'font.size':12})
    #fig.tight_layout()
    filename='_lam%5.2f_nv%5.2f_slr%5.3f_invp0_%5.2e_p0_%5.2e_pmax%5.2e_recharge%5.2e_sgini%5.2e' %(lam,nv,slr,inv_p0,p_air_pa,pmax,recharge_rate_mmPday,sg_init )
    filename=filename.replace('+','').replace('e-','n').replace(' ','')
    plt.savefig('figure/prrm_'+ filename+ '_time_'+str(i)+'_result.png',dpi=200) 
    #i+=200
    #i+=276
    i+=60
    plt.close('all')



# use the command
#ls | cat -n | while read n f; do mv "$f" "$(printf "%05d" $n).png"; done
#ffmpeg -r 3/1 -start_number 101 -i output_%03d.png -c:v libx264 -r 30 -pix_fmt yuv420p output.mp4
