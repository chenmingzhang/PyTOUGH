# this script validate the swcc curve



dat=inp

capillarity_parameter           = dat.grid.rocktype['SAND '].capillarity['parameters']
capillarity_type                = dat.grid.rocktype['SAND '].capillarity['type']
relative_permeability_parameter = dat.grid.rocktype['SAND '].relative_permeability['parameters']
relative_permeability_type      = dat.grid.rocktype['SAND '].relative_permeability['type']


lamda                       = capillarity_parameter[0]
liquid_residual_saturation  = capillarity_parameter[1]

p_zero_point                = 1./capillarity_parameter[2]
pressure_max                = capillarity_parameter[3]
saturated_liquid_saturation = capillarity_parameter[4]

p_zero                      = np.linspace(p_zero_point-1500,p_zero_point+1500,5)     # what is p_zero




#saturation1 = np.linspace(liquid_residual_saturation,saturated_liquid_saturation,100)
saturation1  = np.linspace(liquid_residual_saturation+1.e-5,1,100)     # sat from residue to 1
#saturation2 = np.linspace(0,liquid_residual_saturation,100)
saturation2  = np.linspace(0,liquid_residual_saturation,50)            # sat from 0 to residue




s_star              = (saturation1-liquid_residual_saturation)/(saturated_liquid_saturation-liquid_residual_saturation)


capillary_pressure1 = np.array([1*p_zero[j]*(s_star**(-1/lamda)-1)**(1-lamda) for j in range(len(p_zero))])

sbar                = 1.e-5/(saturated_liquid_saturation-liquid_residual_saturation)
pce                 = np.array([p_zero[j]*(sbar**(-1/lamda)-1)**(1-lamda) for j in range(len(p_zero))])
envg                = 1./(1-lamda)
pcslope             = np.array(
			[-p_zero[j]/lamda/envg/(saturated_liquid_saturation-liquid_residual_saturation)*(sbar**(-1/lamda)-1)**((1-envg)/envg)*sbar**(-(1+lamda)/lamda) 
 			for j in range(len(p_zero))
			])

capillary_pressure2 = np.array([pce[j]+pcslope[j]*(saturation2-liquid_residual_saturation-1.e-5) for j in range(len(p_zero))])



j=2
fig = plt.figure()
ax  = fig.add_subplot(111)
plt.plot(saturation1,capillary_pressure1[j],'r.-',saturation2,capillary_pressure2[j],'.-')
plt.plot(sl_xt_mtx[:,-1],     -pcap_xt_mtx_pa[:,-1],'b.-')

plt.text(0.2, 10.e4*10**(j/1.5),'p_zero='+str(p_zero[j]))
plt.xlabel('saturation')
plt.ylabel('capillary_pressure')
#plt.ylim(10,1.e10)
#plt.xlim(-0.1,1.1)
#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
ax.set_yscale('log')



plt.savefig("figure/Capillary_&_SWCC_for_"+str(i)+".png",dpi=300)


