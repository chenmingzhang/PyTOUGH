import os # this script plots the output times.  #for ii in opt.times[-1]: plt.rcParams["axes.labelweight"] = "bold"
import pandas as pd
if not os.path.exists('figure'):
        os.makedirs('figure')
#reshape_format=[11,7]
#y_mtx=aqui_con.element.DataFrame['Y'][1:].values.reshape(reshape_format)
#x_ay=aqui_con.element.DataFrame['X'].values


#def plot_mineral_profile(ax_idx=ax[15], mineral_name='siderite',sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx ):
#    if any(mineral_name == s for s in sod_input.element.column_name):
#        i = opt_idx[0] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
#        i = opt_idx[1] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
#        i = opt_idx[2] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
#        i = opt_idx[3] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
#        i = opt_idx[4] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
#        i = opt_idx[5] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
#
#        ax_idx.set_xlabel('sod_'+ mineral_name ,fontweight='bold',fontsize=8)
#        ax_idx.invert_yaxis()
#        ax_idx.set_ylabel('Depth (m)' , fontweight='bold')


def plot_aqua_profile(ax_idx=ax[1 ], aqu_name='pH',aqu_input=aqui_con,xlim=None,ylim=None):  #,ele_depth_m=ele_depth_m,opt_idx=opt_idx ):
    if any(aqu_name == s for s in aqui_con.element.column_name):
        im0 = ax_idx.plot(aqu_input.tx_mtx['X'][0],aqu_input.tx_mtx[aqu_name][0],label="%.1e" % aqu_input.times[0]+'yrs')
        im0 = ax_idx.plot(aqu_input.tx_mtx['X'][1],aqu_input.tx_mtx[aqu_name][1],label="%.1e" % aqu_input.times[1]+'yrs')
        im0 = ax_idx.plot(aqu_input.tx_mtx['X'][2],aqu_input.tx_mtx[aqu_name][2],label="%.1e" % aqu_input.times[2]+'yrs')
        im0 = ax_idx.plot(aqu_input.tx_mtx['X'][3],aqu_input.tx_mtx[aqu_name][3],label="%.1e" % aqu_input.times[3]+'yrs')
        im0 = ax_idx.plot(aqu_input.tx_mtx['X'][4],aqu_input.tx_mtx[aqu_name][4],label="%.1e" % aqu_input.times[4]+'yrs')
        im0 = ax_idx.plot(aqu_input.tx_mtx['X'][5],aqu_input.tx_mtx[aqu_name][5],label="%.1e" % aqu_input.times[5]+'yrs')
        im0 = ax_idx.plot(aqu_input.tx_mtx['X'][6],aqu_input.tx_mtx[aqu_name][6],label="%.1e" % aqu_input.times[6]+'yrs')

        ax_idx.set_ylabel('aqu_'+ aqu_name ,fontweight='bold',fontsize=8)
        #ax_idx.invert_yaxis()
        ax_idx.set_xlabel('X (m)' , fontweight='bold',fontsize=8)
        ax_idx.set_title('aqui_con_ '+aqu_name  ,fontweight='bold')
        if xlim !=None:
            ax_idx.set_xlim(xlim)
        if ylim !=None:
            ax_idx.set_ylim(ylim)

def plot_mineral_profile(ax_idx=ax[1 ], min_name='pH',min_input=aqui_min,xlim=None,ylim=None):  #,ele_depth_m=ele_depth_m,opt_idx=opt_idx ):
    if any(min_name == s for s in aqui_min.element.column_name):
        im0 = ax_idx.plot(min_input.tx_mtx['X'][0],min_input.tx_mtx[min_name][0],label="%.1e" % min_input.times[0]+'yrs')
        im0 = ax_idx.plot(min_input.tx_mtx['X'][1],min_input.tx_mtx[min_name][1],label="%.1e" % min_input.times[1]+'yrs')
        im0 = ax_idx.plot(min_input.tx_mtx['X'][2],min_input.tx_mtx[min_name][2],label="%.1e" % min_input.times[2]+'yrs')
        im0 = ax_idx.plot(min_input.tx_mtx['X'][3],min_input.tx_mtx[min_name][3],label="%.1e" % min_input.times[3]+'yrs')
        im0 = ax_idx.plot(min_input.tx_mtx['X'][4],min_input.tx_mtx[min_name][4],label="%.1e" % min_input.times[4]+'yrs')
        im0 = ax_idx.plot(min_input.tx_mtx['X'][5],min_input.tx_mtx[min_name][5],label="%.1e" % min_input.times[5]+'yrs')
        im0 = ax_idx.plot(min_input.tx_mtx['X'][6],min_input.tx_mtx[min_name][6],label="%.1e" % min_input.times[6]+'yrs')

        ax_idx.set_ylabel('min_'+ min_name ,fontweight='bold',fontsize=8)
        ax_idx.set_xlabel('X (m)' , fontweight='bold',fontsize=8)
        ax_idx.set_title('min_con_ '+min_name  ,fontweight='bold')
        if xlim !=None:
            ax_idx.set_xlim(xlim)
        if ylim !=None:
            ax_idx.set_ylim(ylim)

opt.first(); aqui_gas.first(); aqui_min.first(); aqui_con.first()
## ignore the first initial value.
#a=opt.next()
#aqui_gas.next()
#aqui_min.next()
#aqui_con.next()
#opt_pd_max=opt.element.DataFrame.max()
#gas_pd_max=aqui_gas.element.DataFrame.max()
#sod_pd_max=aqui_min.element.DataFrame.max()
#aqu_pd_max=aqui_con.element.DataFrame.max()
#opt_pd_min=opt.element.DataFrame.min()
#gas_pd_min=aqui_gas.element.DataFrame.min()
#sod_pd_min=aqui_min.element.DataFrame.min()
#aqu_pd_min=aqui_con.element.DataFrame.min()


#while a==True:
#    a=opt.element.DataFrame.max()
#    opt_pd_max=pd.concat([opt_pd_max,a],axis=1)
#    a=opt.element.DataFrame.min()
#    opt_pd_min=pd.concat([opt_pd_min,a],axis=1)
#
#    a=aqui_gas.element.DataFrame.max()
#    gas_pd_max=pd.concat([gas_pd_max,a],axis=1)
#    a=aqui_gas.element.DataFrame.min()
#    gas_pd_min=pd.concat([gas_pd_min,a],axis=1)
#
#    a=aqui_min.element.DataFrame.max()
#    sod_pd_max=pd.concat([sod_pd_max,a],axis=1)
#    a=aqui_min.element.DataFrame.min()
#    sod_pd_min=pd.concat([sod_pd_min,a],axis=1)
#
#    a=aqui_con.element.DataFrame.max()
#    aqu_pd_max=pd.concat([aqu_pd_max,a],axis=1)
#    a=aqui_con.element.DataFrame.min()
#    aqu_pd_min=pd.concat([aqu_pd_min,a],axis=1)
#    a=opt.next()
#    aqui_gas.next()
#    aqui_min.next()
#    aqui_con.next()
#    
#
#opt_max_ay=opt_pd_max.max(axis=1);opt_min_ay=opt_pd_min.min(axis=1)
#gas_max_ay=gas_pd_max.max(axis=1);gas_min_ay=gas_pd_min.min(axis=1)
#aqu_max_ay=aqu_pd_max.max(axis=1);aqu_min_ay=aqu_pd_min.min(axis=1)
#sod_max_ay=sod_pd_max.max(axis=1);sod_min_ay=sod_pd_min.min(axis=1)




opt.first();
aqui_gas.first(); aqui_min.first(); aqui_con.first()
plot_every=1
array_length=len(opt.element.DataFrame)


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
aqui_con.first()
aqui_con.tx_mtx={}
for j in aqui_con.element.column_name:
    aqui_con.tx_mtx[j] =np.empty((0,array_length), float) 

for i in aqui_con.times:
    for j in aqui_con.element.column_name:
        aqui_con.tx_mtx[j] =  np.append(aqui_con.tx_mtx[j] , np.array([aqui_con.element.DataFrame[j]]), axis=0)
    aqui_con.next()
    

# aquifer mineral time x axis matrix
aqui_min.tx_mtx={}
for j in aqui_min.element.column_name:
    aqui_min.tx_mtx[j] =np.empty((0,array_length), float) 
for i in aqui_min.times:
    for j in aqui_min.element.column_name:
        aqui_min.tx_mtx[j] =  np.append(aqui_min.tx_mtx[j] , np.array([aqui_min.element.DataFrame[j]]), axis=0)
    aqui_min.next()

# aquifer gas time x axis matrix
aqui_gas.tx_mtx={}
for j in aqui_gas.element.column_name:
    aqui_gas.tx_mtx[j] =np.empty((0,array_length), float) 
for i in aqui_gas.times:
    for j in aqui_gas.element.column_name:
        aqui_gas.tx_mtx[j] =  np.append(aqui_gas.tx_mtx[j] , np.array([aqui_gas.element.DataFrame[j]]), axis=0)
    aqui_gas.next()


connection_x_location= np.vstack([aqui_min.tx_mtx['X'][0][1:], aqui_min.tx_mtx['X'][0][:-1]]).mean(axis=0)

aqui_gas.first(); aqui_min.first(); aqui_con.first()
#for ii in opt.times[0::plot_every]:

fig = plt.figure(figsize=(16,12))
   
tlt =('opt.time='  "%0.2f" % (opt.time/86400/365)   +' years' 
    + ', sod.time='  "%0.2f" % (aqui_min.time   ) +' years'
    ', aqu.time='  "%0.2f" % (aqui_con.time   ) +' years'
    ', aqu.time='  "%0.2f" % (aqui_gas.time   ) +' years')
#fig.suptitle(   tlt     , fontsize=16,fontweight="bold")
print(tlt)
no_row=6
no_col=4
ax = [[] for i in range(no_row*no_col)]

k=0
for i in np.arange(no_row):
    for j in np.arange(no_col):
        ax[k]= plt.subplot2grid((no_row, no_col), (i, j), colspan=1)
        ax[k].xaxis.set_tick_params(labelsize=10)
        ax[k].yaxis.set_tick_params(labelsize=10)
        k+=1
        

fig.subplots_adjust(hspace=.50,wspace=.5)
fig.subplots_adjust(left=0.05, right=0.90, top=0.92, bottom=0.05)

##aqui_con.get_index() --> get the current index number
## aqui_gas.element.column_name
#['row', 'X', 'Y', 'Z', 'P(bar)', 'Sg', 'Sl', 'T(C)', 'aH2O', 'pH', 't_ca+2', 't_mg+2', 't_na+', 't_cl-', 't_sio2(aq)', 't_hco3-', 't_so4-2', 't_k+', 't_alo2-', 't_fe+2']

#im0 = ax[0].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['pH'][0],label="%.1e" % aqui_con.times[0]+'yrs')
#im0 = ax[0].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['pH'][1],label="%.1e" % aqui_con.times[1]+'yrs')
#im0 = ax[0].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['pH'][2],label="%.1e" % aqui_con.times[2]+'yrs')
#im0 = ax[0].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['pH'][3],label="%.1e" % aqui_con.times[3]+'yrs')
#im0 = ax[0].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['pH'][4],label="%.1e" % aqui_con.times[4]+'yrs')
#im0 = ax[0].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['pH'][5],label="%.1e" % aqui_con.times[5]+'yrs')



#im1 = ax[1].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['T(C)'][0])
#im1 = ax[1].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['T(C)'][1])
#im1 = ax[1].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['T(C)'][2])
#im1 = ax[1].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['T(C)'][3])
#im1 = ax[1].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['T(C)'][4])
#im1 = ax[1].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['T(C)'][5])


plot_aqua_profile(ax_idx=ax[ 0], aqu_name='t_k+'      , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 1], aqu_name='pH'        , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 2], aqu_name='t_ca+2'    , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 3], aqu_name='t_mg+2'    , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 4], aqu_name='t_na+'     , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 5], aqu_name='t_hco3-'   , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 6], aqu_name='t_cl-'     , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 7], aqu_name='t_sio2(aq)', aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 8], aqu_name='t_so4-2'   , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[ 9], aqu_name='t_alo2-'   , aqu_input=aqui_con,xlim=[0.5,1.2])
plot_aqua_profile(ax_idx=ax[10], aqu_name='t_fe+2'    , aqu_input=aqui_con,xlim=[0.5,1.2])
ax[3].legend(bbox_to_anchor=(1.02, 0.9), loc=2, borderaxespad=0.)


##aqui_min.element.column_name
##['X', 'Y', 'Z', 'T(C)', 'Porosity', 'Poros_Chg', 'Permx(m^2)', 'Kx/Kx0', 'Permz(m^2)', 'Kz/Kz0', 'calcite']
#['X', 'Y', 'Z', 'T(C)', 'Porosity', 'Poros_Chg', 'Permx(m^2)', 'Kx/Kx0', 'Permz(m^2)', 'Kz/Kz0', 'calcite', 'anhydrite', 'k-feldspar', 'quartz', 'annite', 'montmorillonite-na',
# 'montmorillonite-ca', 'sio2(am)_g', 'kaolinite', 'illite', 'chlorite', 'dolomite-2', 'siderite-2']


#im15 = ax[15].plot(aqui_min.tx_mtx['X'][0],aqui_min.tx_mtx['calcite'][0])
#im15 = ax[15].plot(aqui_min.tx_mtx['X'][1],aqui_min.tx_mtx['calcite'][1])
#im15 = ax[15].plot(aqui_min.tx_mtx['X'][2],aqui_min.tx_mtx['calcite'][2])
#im15 = ax[15].plot(aqui_min.tx_mtx['X'][3],aqui_min.tx_mtx['calcite'][3])
#im15 = ax[15].plot(aqui_min.tx_mtx['X'][4],aqui_min.tx_mtx['calcite'][4])
#im15 = ax[15].plot(aqui_min.tx_mtx['X'][5],aqui_min.tx_mtx['calcite'][5])


plot_mineral_profile(ax_idx=ax[11], min_name='quartz'               , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[12], min_name='k-feldspar'           , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[13], min_name='anhydrite'            , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[14], min_name='calcite'              , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[15], min_name='T(C)'                 , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[18], min_name='montmorillonite-na'   , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[19], min_name='montmorillonite-ca'   , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[20], min_name='annite'               , min_input=aqui_min,xlim=[0.5,1.2])
plot_mineral_profile(ax_idx=ax[21], min_name='calcite'              , min_input=aqui_min,xlim=[0.5,1.2],ylim=[-6e-2,4e-2])
plot_mineral_profile(ax_idx=ax[22], min_name='kaolinite'            , min_input=aqui_min,xlim=[0.5,1.2],ylim=[-5e-2,2.5e-1])
plot_mineral_profile(ax_idx=ax[23], min_name='chlorite'             , min_input=aqui_min,xlim=[0.5,1.2],ylim=[-1e-2,4e-2])





im16 = ax[16].plot(connection_x_location,opt.tx_con_mtx['FLO(LIQ.)'][0])
im16 = ax[16].plot(connection_x_location,opt.tx_con_mtx['FLO(LIQ.)'][1])
im16 = ax[16].plot(connection_x_location,opt.tx_con_mtx['FLO(LIQ.)'][2])
im16 = ax[16].plot(connection_x_location,opt.tx_con_mtx['FLO(LIQ.)'][3])
im16 = ax[16].plot(connection_x_location,opt.tx_con_mtx['FLO(LIQ.)'][4])
#im16 = ax[16].plot(connection_x_location,opt.tx_con_mtx['FLO(LIQ.)'][5])

im17 = ax[17].plot(connection_x_location,opt.tx_con_mtx['VEL(LIQ.)'][0])
im17 = ax[17].plot(connection_x_location,opt.tx_con_mtx['VEL(LIQ.)'][1])
im17 = ax[17].plot(connection_x_location,opt.tx_con_mtx['VEL(LIQ.)'][2])
im17 = ax[17].plot(connection_x_location,opt.tx_con_mtx['VEL(LIQ.)'][3])
im17 = ax[17].plot(connection_x_location,opt.tx_con_mtx['VEL(LIQ.)'][4])
#im17 = ax[17].plot(connection_x_location,opt.tx_con_mtx['VEL(LIQ.)'][5])


plt.show(block=False)

#ax[0].scatter(aqui_con.element.DataFrame['X'],aqui_con.element.DataFrame['Y'])

# opt.element.column_name
# ['PRES', 'S(liq)', 'PCAP', 'K(rel)', 'DIFFUS.']
# NOTE: capillary pressure is negative in TOUGH


#flow_first_column_ay=opt.connection.DataFrame.loc[mask_first_column_index_ay]




##aqui_con.element.column_name
##conclusion  aqu_sg_mtx + aqu_sl_mtx  ==1 
##['X', 'Y', 'Z', 'P(bar)', 'Sg', 'Sl', 'T(C)', 'aH2O', 'pH', 't_h2o', 't_h+', 't_ca+2', 't_mg+2', 't_na+', 't_k+', 't_hco3-', 't_so4-2', 't_cl-', 'X_na+', 'X_k+', 'X_ca+2', 'X_mg+2', 'X_h+']


##  a confirmation flow_first_column_ay['FLO(LIQ.)']/sat_liquid_mtx[:-1,0]/flow_first_column_ay['VEL(LIQ.)'] 
## essentially 
## FLO(LIQ.) [kg/s] = por * sat * VEL(LIQ.) [m3/s]  * density   [kg/m3]  
## the unit of FLO(LIQ.) can be confirmated by the lower value as -5e-7 [kg/s], same as the input in GENER.
#    



##fig.colorbar(im44, ax=ax[44], format='%.1e')
##fig.colorbar(im27, ax=ax[27])
##fig.colorbar(im28, ax=ax[28])
##fig.colorbar(im29, ax=ax[29])

output_name = 'figure/'+current_folder_name+'.jpg'
fig.savefig(output_name, format='jpg', dpi=100)

#for i in np.arange(plot_every):
#    opt.next()
#    aqui_gas.next()
#    aqui_min.next()
#    aqui_con.next()
    


