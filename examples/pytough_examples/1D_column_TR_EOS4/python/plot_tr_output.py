import os # this script plots the output times.  #for ii in opt.times[-1]: plt.rcParams["axes.labelweight"] = "bold"
import pandas as pd
if not os.path.exists('figure'):
        os.makedirs('figure')
#reshape_format=[11,7]
#y_mtx=aqu.element.DataFrame['Y'][1:].values.reshape(reshape_format)
x_ay=aqu.element.DataFrame['X'].values
y_ay=aqu.element.DataFrame['Y'].values

opt.first(); gas.first(); aqu.first(); sod.first()
## ignore the first initial value.
#a=opt.next()
#gas.next()
#sod.next()
#aqu.next()
#opt_pd_max=opt.element.DataFrame.max()
#gas_pd_max=gas.element.DataFrame.max()
#sod_pd_max=sod.element.DataFrame.max()
#aqu_pd_max=aqu.element.DataFrame.max()
#opt_pd_min=opt.element.DataFrame.min()
#gas_pd_min=gas.element.DataFrame.min()
#sod_pd_min=sod.element.DataFrame.min()
#aqu_pd_min=aqu.element.DataFrame.min()


#while a==True:
#    a=opt.element.DataFrame.max()
#    opt_pd_max=pd.concat([opt_pd_max,a],axis=1)
#    a=opt.element.DataFrame.min()
#    opt_pd_min=pd.concat([opt_pd_min,a],axis=1)
#
#    a=gas.element.DataFrame.max()
#    gas_pd_max=pd.concat([gas_pd_max,a],axis=1)
#    a=gas.element.DataFrame.min()
#    gas_pd_min=pd.concat([gas_pd_min,a],axis=1)
#
#    a=sod.element.DataFrame.max()
#    sod_pd_max=pd.concat([sod_pd_max,a],axis=1)
#    a=sod.element.DataFrame.min()
#    sod_pd_min=pd.concat([sod_pd_min,a],axis=1)
#
#    a=aqu.element.DataFrame.max()
#    aqu_pd_max=pd.concat([aqu_pd_max,a],axis=1)
#    a=aqu.element.DataFrame.min()
#    aqu_pd_min=pd.concat([aqu_pd_min,a],axis=1)
#    a=opt.next()
#    gas.next()
#    sod.next()
#    aqu.next()
#    
#
#opt_max_ay=opt_pd_max.max(axis=1);opt_min_ay=opt_pd_min.min(axis=1)
#gas_max_ay=gas_pd_max.max(axis=1);gas_min_ay=gas_pd_min.min(axis=1)
#aqu_max_ay=aqu_pd_max.max(axis=1);aqu_min_ay=aqu_pd_min.min(axis=1)
#sod_max_ay=sod_pd_max.max(axis=1);sod_min_ay=sod_pd_min.min(axis=1)




opt.first();
gas.first(); sod.first(); aqu.first()
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
con_depth_m= np.vstack([sod.tx_mtx['Z'][0][1:], sod.tx_mtx['Z'][0][:-1]]).mean(axis=0)

gas.first(); sod.first(); aqu.first()
#for ii in opt.times[0::plot_every]:

fig = plt.figure(figsize=(16,12))
   
tlt =('opt.time='  "%0.2f" % (opt.time/86400/365)   +' years' 
    + ', sod.time='  "%0.2f" % (sod.time   ) +' years'
    ', aqu.time='  "%0.2f" % (aqu.time   ) +' years'
    ', aqu.time='  "%0.2f" % (gas.time   ) +' years')
#fig.suptitle(   tlt     , fontsize=16,fontweight="bold")
print(tlt)
no_row=5
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

##aqu.get_index() --> get the current index number
## gas.element.column_name
#['X', 'Y', 'Z', 'P(bar)', 'Sg', 'Sl', 'T(C)', 'aH2O', 'pH', 't_h2o', 't_h+', 't_ca+2', 't_mg+2', 
#'t_na+', 't_k+', 't_hco3-', 't_so4-2', 't_cl-', 'X_na+', 'X_k+', 'X_ca+2', 'X_mg+2', 'X_h+']
i = opt_idx[0]; im0 = ax[0].plot( aqu.tx_mtx['pH'][i] , ele_depth_m , label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[1]; im0 = ax[0].plot( aqu.tx_mtx['pH'][i] , ele_depth_m , label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[2]; im0 = ax[0].plot( aqu.tx_mtx['pH'][i] , ele_depth_m , label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[3]; im0 = ax[0].plot( aqu.tx_mtx['pH'][i] , ele_depth_m , label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[4]; im0 = ax[0].plot( aqu.tx_mtx['pH'][i] , ele_depth_m , label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[5]; im0 = ax[0].plot( aqu.tx_mtx['pH'][i] , ele_depth_m , label="%.1e" % aqu.times[i]+'yrs')



# what does it mean by 't_h20' 
i = opt_idx[0] ; im1 = ax[1].plot( aqu.tx_mtx['t_h2o'][i] , ele_depth_m )
i = opt_idx[1] ; im1 = ax[1].plot( aqu.tx_mtx['t_h2o'][i] , ele_depth_m )
i = opt_idx[2] ; im1 = ax[1].plot( aqu.tx_mtx['t_h2o'][i] , ele_depth_m )
i = opt_idx[3] ; im1 = ax[1].plot( aqu.tx_mtx['t_h2o'][i] , ele_depth_m )
i = opt_idx[4] ; im1 = ax[1].plot( aqu.tx_mtx['t_h2o'][i] , ele_depth_m )
i = opt_idx[5] ; im1 = ax[1].plot( aqu.tx_mtx['t_h2o'][i] , ele_depth_m )



i = opt_idx[0] ; im2 = ax[2].plot( aqu.tx_mtx['t_h+'][i] , ele_depth_m )
i = opt_idx[1] ; im2 = ax[2].plot( aqu.tx_mtx['t_h+'][i] , ele_depth_m )
i = opt_idx[2] ; im2 = ax[2].plot( aqu.tx_mtx['t_h+'][i] , ele_depth_m )
i = opt_idx[3] ; im2 = ax[2].plot( aqu.tx_mtx['t_h+'][i] , ele_depth_m )
i = opt_idx[4] ; im2 = ax[2].plot( aqu.tx_mtx['t_h+'][i] , ele_depth_m )
i = opt_idx[5] ; im2 = ax[2].plot( aqu.tx_mtx['t_h+'][i] , ele_depth_m )



i = opt_idx[0] ; im3 = ax[3].plot( aqu.tx_mtx['pH'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[1] ; im3 = ax[3].plot( aqu.tx_mtx['pH'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[2] ; im3 = ax[3].plot( aqu.tx_mtx['pH'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[3] ; im3 = ax[3].plot( aqu.tx_mtx['pH'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[4] ; im3 = ax[3].plot( aqu.tx_mtx['pH'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[5] ; im3 = ax[3].plot( aqu.tx_mtx['pH'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
#im3 = ax[3].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['pH']['ctot'] )

ax[3].legend(bbox_to_anchor=(1.02, 0.9), loc=2, borderaxespad=0.)

#im4 = ax[4].plot(aqu.tx_mtx['X'][0] , aqu.tx_mtx['t_mg+2'][0])
#im4 = ax[4].plot(aqu.tx_mtx['X'][1] , aqu.tx_mtx['t_mg+2'][1])
#im4 = ax[4].plot(aqu.tx_mtx['X'][2] , aqu.tx_mtx['t_mg+2'][2])
#im4 = ax[4].plot(aqu.tx_mtx['X'][3] , aqu.tx_mtx['t_mg+2'][3])
#im4 = ax[4].plot(aqu.tx_mtx['X'][4] , aqu.tx_mtx['t_mg+2'][4])
#im4 = ax[4].plot(aqu.tx_mtx['X'][5] , aqu.tx_mtx['t_mg+2'][5])
#im4 = ax[4].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['mg+2']['ctot'] )

#im5 = ax[5].plot(aqu.tx_mtx['X'][0] , aqu.tx_mtx['t_na+'][0])
#im5 = ax[5].plot(aqu.tx_mtx['X'][1] , aqu.tx_mtx['t_na+'][1])
#im5 = ax[5].plot(aqu.tx_mtx['X'][2] , aqu.tx_mtx['t_na+'][2])
#im5 = ax[5].plot(aqu.tx_mtx['X'][3] , aqu.tx_mtx['t_na+'][3])
#im5 = ax[5].plot(aqu.tx_mtx['X'][4] , aqu.tx_mtx['t_na+'][4])
#im5 = ax[5].plot(aqu.tx_mtx['X'][5] , aqu.tx_mtx['t_na+'][5])
#im5 = ax[5].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['na+']['ctot'] )
#
#im6 = ax[6].plot(aqu.tx_mtx['X'][0] , aqu.tx_mtx['t_k+'][0])
#im6 = ax[6].plot(aqu.tx_mtx['X'][1] , aqu.tx_mtx['t_k+'][1])
#im6 = ax[6].plot(aqu.tx_mtx['X'][2] , aqu.tx_mtx['t_k+'][2])
#im6 = ax[6].plot(aqu.tx_mtx['X'][3] , aqu.tx_mtx['t_k+'][3])
#im6 = ax[6].plot(aqu.tx_mtx['X'][4] , aqu.tx_mtx['t_k+'][4])
#im6 = ax[6].plot(aqu.tx_mtx['X'][5] , aqu.tx_mtx['t_k+'][5])
#im6 = ax[6].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['k+']['ctot'] )
#
#im7 = ax[7].plot(aqu.tx_mtx['X'][0] , aqu.tx_mtx['t_hco3-'][0])
#im7 = ax[7].plot(aqu.tx_mtx['X'][1] , aqu.tx_mtx['t_hco3-'][1])
#im7 = ax[7].plot(aqu.tx_mtx['X'][2] , aqu.tx_mtx['t_hco3-'][2])
#im7 = ax[7].plot(aqu.tx_mtx['X'][3] , aqu.tx_mtx['t_hco3-'][3])
#im7 = ax[7].plot(aqu.tx_mtx['X'][4] , aqu.tx_mtx['t_hco3-'][4])
#im7 = ax[7].plot(aqu.tx_mtx['X'][5] , aqu.tx_mtx['t_hco3-'][5])
#im7 = ax[7].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['hco3-']['ctot'] )

i = opt_idx[0] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
i = opt_idx[1] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
i = opt_idx[2] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
i = opt_idx[3] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
i = opt_idx[4] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
i = opt_idx[5] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
#im8 = ax[8].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['so4-2']['ctot'] )

#im9 = ax[9].plot(aqu.tx_mtx['X'][0],aqu.tx_mtx['t_cl-'][0])
#im9 = ax[9].plot(aqu.tx_mtx['X'][1],aqu.tx_mtx['t_cl-'][1])
#im9 = ax[9].plot(aqu.tx_mtx['X'][2],aqu.tx_mtx['t_cl-'][2])
#im9 = ax[9].plot(aqu.tx_mtx['X'][3],aqu.tx_mtx['t_cl-'][3])
#im9 = ax[9].plot(aqu.tx_mtx['X'][4],aqu.tx_mtx['t_cl-'][4])
#im9 = ax[9].plot(aqu.tx_mtx['X'][5],aqu.tx_mtx['t_cl-'][5])
#im9 = ax[9].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['cl-']['ctot'] )

#im10 = ax[10].plot(aqu.tx_mtx['X'][0],aqu.tx_mtx['X_na+'][0])
#im10 = ax[10].plot(aqu.tx_mtx['X'][1],aqu.tx_mtx['X_na+'][1])
#im10 = ax[10].plot(aqu.tx_mtx['X'][2],aqu.tx_mtx['X_na+'][2])
#im10 = ax[10].plot(aqu.tx_mtx['X'][3],aqu.tx_mtx['X_na+'][3])
#im10 = ax[10].plot(aqu.tx_mtx['X'][4],aqu.tx_mtx['X_na+'][4])
#im10 = ax[10].plot(aqu.tx_mtx['X'][5],aqu.tx_mtx['X_na+'][5])

#im11 = ax[11].plot(aqu.tx_mtx['X'][0],aqu.tx_mtx['X_k+'][0])
#im11 = ax[11].plot(aqu.tx_mtx['X'][1],aqu.tx_mtx['X_k+'][1])
#im11 = ax[11].plot(aqu.tx_mtx['X'][2],aqu.tx_mtx['X_k+'][2])
#im11 = ax[11].plot(aqu.tx_mtx['X'][3],aqu.tx_mtx['X_k+'][3])
#im11 = ax[11].plot(aqu.tx_mtx['X'][4],aqu.tx_mtx['X_k+'][4])
#im11 = ax[11].plot(aqu.tx_mtx['X'][5],aqu.tx_mtx['X_k+'][5])

#im12 = ax[12].plot(aqu.tx_mtx['X'][0],aqu.tx_mtx['X_ca+2'][0])
#im12 = ax[12].plot(aqu.tx_mtx['X'][1],aqu.tx_mtx['X_ca+2'][1])
#im12 = ax[12].plot(aqu.tx_mtx['X'][2],aqu.tx_mtx['X_ca+2'][2])
#im12 = ax[12].plot(aqu.tx_mtx['X'][3],aqu.tx_mtx['X_ca+2'][3])
#im12 = ax[12].plot(aqu.tx_mtx['X'][4],aqu.tx_mtx['X_ca+2'][4])
#im12 = ax[12].plot(aqu.tx_mtx['X'][5],aqu.tx_mtx['X_ca+2'][5])

#im13 = ax[13].plot(aqu.tx_mtx['X'][0],aqu.tx_mtx['X_mg+2'][0])
#im13 = ax[13].plot(aqu.tx_mtx['X'][1],aqu.tx_mtx['X_mg+2'][1])
#im13 = ax[13].plot(aqu.tx_mtx['X'][2],aqu.tx_mtx['X_mg+2'][2])
#im13 = ax[13].plot(aqu.tx_mtx['X'][3],aqu.tx_mtx['X_mg+2'][3])
#im13 = ax[13].plot(aqu.tx_mtx['X'][4],aqu.tx_mtx['X_mg+2'][4])
#im13 = ax[13].plot(aqu.tx_mtx['X'][5],aqu.tx_mtx['X_mg+2'][5])

#im14 = ax[14].plot(aqu.tx_mtx['X'][0],aqu.tx_mtx['X_h+'][0])
#im14 = ax[14].plot(aqu.tx_mtx['X'][1],aqu.tx_mtx['X_h+'][1])
#im14 = ax[14].plot(aqu.tx_mtx['X'][2],aqu.tx_mtx['X_h+'][2])
#im14 = ax[14].plot(aqu.tx_mtx['X'][3],aqu.tx_mtx['X_h+'][3])
#im14 = ax[14].plot(aqu.tx_mtx['X'][4],aqu.tx_mtx['X_h+'][4])
#im14 = ax[14].plot(aqu.tx_mtx['X'][5],aqu.tx_mtx['X_h+'][5])

##sod.element.column_name
##['X', 'Y', 'Z', 'T(C)', 'Porosity', 'Poros_Chg', 'Permx(m^2)', 'Kx/Kx0', 'Permz(m^2)', 'Kz/Kz0', 'calcite']

i = opt_idx[0] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
i = opt_idx[1] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
i = opt_idx[2] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
i = opt_idx[3] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
i = opt_idx[4] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
i = opt_idx[5] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)

#list(opt.tx_con_mtx)
#['FLOH', 'FLOH/FLOF', 'FLOF', 'FLO(GAS)', 'VAPDIF', 'FLO(LIQ.)', 'VEL(GAS)', 'VEL(LIQ.)']

i = opt_idx[0] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i], con_depth_m)
i = opt_idx[1] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i], con_depth_m)
i = opt_idx[2] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i], con_depth_m)
i = opt_idx[3] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i], con_depth_m)
i = opt_idx[4] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i], con_depth_m)
i = opt_idx[5] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i], con_depth_m)

i = opt_idx[0] ; im17 = ax[17].plot(opt.tx_con_mtx['VEL(LIQ.)'][i],con_depth_m)
i = opt_idx[1] ; im17 = ax[17].plot(opt.tx_con_mtx['VEL(LIQ.)'][i],con_depth_m)
i = opt_idx[2] ; im17 = ax[17].plot(opt.tx_con_mtx['VEL(LIQ.)'][i],con_depth_m)
i = opt_idx[3] ; im17 = ax[17].plot(opt.tx_con_mtx['VEL(LIQ.)'][i],con_depth_m)
i = opt_idx[4] ; im17 = ax[17].plot(opt.tx_con_mtx['VEL(LIQ.)'][i],con_depth_m)
i = opt_idx[5] ; im17 = ax[17].plot(opt.tx_con_mtx['VEL(LIQ.)'][i],con_depth_m)

i = opt_idx[0] ; im16 = ax[18].plot(opt.tx_con_mtx['FLO(GAS)'][i], con_depth_m)
i = opt_idx[1] ; im16 = ax[18].plot(opt.tx_con_mtx['FLO(GAS)'][i], con_depth_m)
i = opt_idx[2] ; im16 = ax[18].plot(opt.tx_con_mtx['FLO(GAS)'][i], con_depth_m)
i = opt_idx[3] ; im16 = ax[18].plot(opt.tx_con_mtx['FLO(GAS)'][i], con_depth_m)
i = opt_idx[4] ; im16 = ax[18].plot(opt.tx_con_mtx['FLO(GAS)'][i], con_depth_m)
i = opt_idx[5] ; im16 = ax[18].plot(opt.tx_con_mtx['FLO(GAS)'][i], con_depth_m)

i = opt_idx[0] ; im17 = ax[19].plot(opt.tx_con_mtx['VEL(GAS)'][i],con_depth_m)
i = opt_idx[1] ; im17 = ax[19].plot(opt.tx_con_mtx['VEL(GAS)'][i],con_depth_m)
i = opt_idx[2] ; im17 = ax[19].plot(opt.tx_con_mtx['VEL(GAS)'][i],con_depth_m)
i = opt_idx[3] ; im17 = ax[19].plot(opt.tx_con_mtx['VEL(GAS)'][i],con_depth_m)
i = opt_idx[4] ; im17 = ax[19].plot(opt.tx_con_mtx['VEL(GAS)'][i],con_depth_m)
i = opt_idx[5] ; im17 = ax[19].plot(opt.tx_con_mtx['VEL(GAS)'][i],con_depth_m)
plt.show(block=False)

#ax[0].scatter(aqu.element.DataFrame['X'],aqu.element.DataFrame['Y'])

# opt.element.column_name
# ['PRES', 'S(liq)', 'PCAP', 'K(rel)', 'DIFFUS.']
# NOTE: capillary pressure is negative in TOUGH


#flow_first_column_ay=opt.connection.DataFrame.loc[mask_first_column_index_ay]




##aqu.element.column_name
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
ax[0 ].set_title('aqu_ pH'     ,fontweight='bold')
ax[1 ].set_title('aqu_ t_h20'  ,fontweight='bold')
ax[2 ].set_title('aqu_ t_h+'   ,fontweight='bold')
ax[3 ].set_title('aqu_ t_ca+2' ,fontweight='bold')
ax[4 ].set_title('aqu_ t_mg+2' ,fontweight='bold')
ax[5 ].set_title('aqu_ t_na+'  ,fontweight='bold')
ax[6 ].set_title('aqu_ t_k+'   ,fontweight='bold')
ax[7 ].set_title('aqu_ t_hco3-',fontweight='bold')
ax[8 ].set_title('aqu_ t_so4-2',fontweight='bold')
ax[9 ].set_title('aqu_ t_cl-'  ,fontweight='bold')
ax[10].set_title('aqu_ X_na+'  ,fontweight='bold')
ax[11].set_title('aqu_ X_k+'   ,fontweight='bold')
ax[12].set_title('aqu_ X_ca+2' ,fontweight='bold')
ax[13].set_title('aqu_ X_mg+2' ,fontweight='bold')
ax[14].set_title('aqu_ X_h+'   ,fontweight='bold')
ax[15].set_title('sod_pyrite'  ,fontweight='bold')
ax[16].set_title('opt_FLO(LIQ)',fontweight='bold')
ax[17].set_title('opt_VEL(LIQ)',fontweight='bold')


# unit is given from aqu.dat header
ax[0 ].set_ylabel('pH'     ,fontweight='bold')
ax[1 ].set_ylabel('t_h20  \n mol/L'  ,fontweight='bold')
ax[2 ].set_ylabel('t_h+   \n mol/L'   ,fontweight='bold')
ax[3 ].set_ylabel('t_ca+2 \n mol/L' ,fontweight='bold')
ax[4 ].set_ylabel('t_mg+2 \n mol/L' ,fontweight='bold')
ax[5 ].set_ylabel('t_na+  \n mol/L'  ,fontweight='bold')
ax[6 ].set_ylabel('t_k+   \n mol/L'   ,fontweight='bold')
ax[7 ].set_ylabel('t_hco3-\n mol/L',fontweight='bold')
ax[8 ].set_ylabel('t_so4-2\n mol/L',fontweight='bold')
ax[9 ].set_ylabel('t_cl-  \n mol/L'  ,fontweight='bold')
ax[10].set_ylabel('aqu_\n X_na+'  ,fontweight='bold')
ax[11].set_ylabel('aqu_\n X_k+'   ,fontweight='bold')
ax[12].set_ylabel('aqu_\n X_ca+2' ,fontweight='bold')
ax[13].set_ylabel('aqu_\n X_mg+2' ,fontweight='bold')
ax[14].set_ylabel('aqu_\n X_h+'   ,fontweight='bold')
ax[15].set_ylabel('sod_\n calcite',fontweight='bold')
ax[16].set_ylabel('opt_FLO(LIQ)',fontweight='bold')
ax[17].set_ylabel('opt_VEL(LIQ)',fontweight='bold')

#
#ax[27].set_title('flow.out \n FLO(LIQ.)_fra(kg/s)'     , fontweight='bold')
#ax[28].set_title('flow.out \n VEL(LIQ.)_fra(m3/s)'     , fontweight='bold')
#ax[29].set_title('flow.out \n sat_liq_fra'     , fontweight='bold')

#ax[30].set_title('aqu \n t_so4-2'    ,  fontweight='bold') 
#ax[31].set_title('aqu \n t_fe+2'     ,  fontweight='bold') 
#ax[32].set_title('aqu \n t_cu+2'     ,  fontweight='bold') 
#ax[33].set_title('aqu \n t_na+'      ,  fontweight='bold') 
#ax[34].set_title('aqu \n t_k+'       ,  fontweight='bold') 
#ax[35].set_title('aqu \n t_ca+2'     ,  fontweight='bold') 
#ax[36].set_title('aqu \n t_alo2-'    ,  fontweight='bold') 
#ax[37].set_title('aqu \n t_sio2(aq)' ,  fontweight='bold') 
#ax[38].set_title('aqu \n P(bar)'     ,  fontweight='bold') 
#ax[39].set_title('aqu \n Sg'         ,  fontweight='bold') 
#ax[40].set_title('aqu \n Sl'         ,  fontweight='bold') 
#ax[41].set_title('aqu \n T(C)'       ,  fontweight='bold') 
#ax[42].set_title('aqu \n aH2O'       ,  fontweight='bold') 
#ax[43].set_title('aqu \n pH'         ,  fontweight='bold') 
##ax[44].set_title('aqu \n ',  fontweight='bold') 
#ax[45].set_title('aqu \n t_cl-'      ,  fontweight='bold') 

output_name = 'figure/'+'chemcal'+'.jpg'
fig.savefig(output_name, format='jpg', dpi=100)

fig.close()
#for i in np.arange(plot_every):
#    opt.next()
#    gas.next()
#    sod.next()
#    aqu.next()
    


