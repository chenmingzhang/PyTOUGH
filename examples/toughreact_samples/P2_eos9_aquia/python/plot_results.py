import os # this script plots the output times.  #for ii in opt.times[-1]: plt.rcParams["axes.labelweight"] = "bold"
import pandas as pd
if not os.path.exists('figure'):
        os.makedirs('figure')
#reshape_format=[11,7]
#y_mtx=aqui_con.element.DataFrame['Y'][1:].values.reshape(reshape_format)
#x_ay=aqui_con.element.DataFrame['X'].values

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
plot_every=5
array_length=16


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
fig.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.05)

##aqui_con.get_index() --> get the current index number
## aqui_gas.element.column_name
#['X', 'Y', 'Z', 'P(bar)', 'Sg', 'Sl', 'T(C)', 'aH2O', 'pH', 't_h2o', 't_h+', 't_ca+2', 't_mg+2', 
#'t_na+', 't_k+', 't_hco3-', 't_so4-2', 't_cl-', 'X_na+', 'X_k+', 'X_ca+2', 'X_mg+2', 'X_h+']
im0 = ax[0].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['pH'][0],label="%.1e" % aqui_con.times[0]+'yrs')
im0 = ax[0].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['pH'][1],label="%.1e" % aqui_con.times[1]+'yrs')
im0 = ax[0].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['pH'][2],label="%.1e" % aqui_con.times[2]+'yrs')
im0 = ax[0].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['pH'][3],label="%.1e" % aqui_con.times[3]+'yrs')
im0 = ax[0].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['pH'][4],label="%.1e" % aqui_con.times[4]+'yrs')
im0 = ax[0].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['pH'][5],label="%.1e" % aqui_con.times[5]+'yrs')

ax[0].legend(bbox_to_anchor=(1.01, 0.65), loc=2, borderaxespad=0.)

im1 = ax[1].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_h2o'][0])
im1 = ax[1].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_h2o'][1])
im1 = ax[1].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_h2o'][2])
im1 = ax[1].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_h2o'][3])
im1 = ax[1].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_h2o'][4])
im1 = ax[1].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_h2o'][5])


im2 = ax[2].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_h+'][0])
im2 = ax[2].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_h+'][1])
im2 = ax[2].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_h+'][2])
im2 = ax[2].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_h+'][3])
im2 = ax[2].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_h+'][4])
im2 = ax[2].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_h+'][5])


im3 = ax[3].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_ca+2'][0])
im3 = ax[3].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_ca+2'][1])
im3 = ax[3].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_ca+2'][2])
im3 = ax[3].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_ca+2'][3])
im3 = ax[3].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_ca+2'][4])
im3 = ax[3].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_ca+2'][5])


im4 = ax[4].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_mg+2'][0])
im4 = ax[4].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_mg+2'][1])
im4 = ax[4].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_mg+2'][2])
im4 = ax[4].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_mg+2'][3])
im4 = ax[4].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_mg+2'][4])
im4 = ax[4].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_mg+2'][5])

im5 = ax[5].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_na+'][0])
im5 = ax[5].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_na+'][1])
im5 = ax[5].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_na+'][2])
im5 = ax[5].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_na+'][3])
im5 = ax[5].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_na+'][4])
im5 = ax[5].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_na+'][5])

im6 = ax[6].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_k+'][0])
im6 = ax[6].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_k+'][1])
im6 = ax[6].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_k+'][2])
im6 = ax[6].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_k+'][3])
im6 = ax[6].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_k+'][4])
im6 = ax[6].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_k+'][5])

im7 = ax[7].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_hco3-'][0])
im7 = ax[7].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_hco3-'][1])
im7 = ax[7].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_hco3-'][2])
im7 = ax[7].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_hco3-'][3])
im7 = ax[7].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_hco3-'][4])
im7 = ax[7].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_hco3-'][5])


im8 = ax[8].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_so4-2'][0])
im8 = ax[8].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_so4-2'][1])
im8 = ax[8].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_so4-2'][2])
im8 = ax[8].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_so4-2'][3])
im8 = ax[8].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_so4-2'][4])
im8 = ax[8].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_so4-2'][5])


im9 = ax[9].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['t_cl-'][0])
im9 = ax[9].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['t_cl-'][1])
im9 = ax[9].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['t_cl-'][2])
im9 = ax[9].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['t_cl-'][3])
im9 = ax[9].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['t_cl-'][4])
im9 = ax[9].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['t_cl-'][5])

im10 = ax[10].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['X_na+'][0])
im10 = ax[10].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['X_na+'][1])
im10 = ax[10].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['X_na+'][2])
im10 = ax[10].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['X_na+'][3])
im10 = ax[10].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['X_na+'][4])
im10 = ax[10].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['X_na+'][5])

im11 = ax[11].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['X_k+'][0])
im11 = ax[11].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['X_k+'][1])
im11 = ax[11].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['X_k+'][2])
im11 = ax[11].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['X_k+'][3])
im11 = ax[11].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['X_k+'][4])
im11 = ax[11].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['X_k+'][5])

im12 = ax[12].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['X_ca+2'][0])
im12 = ax[12].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['X_ca+2'][1])
im12 = ax[12].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['X_ca+2'][2])
im12 = ax[12].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['X_ca+2'][3])
im12 = ax[12].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['X_ca+2'][4])
im12 = ax[12].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['X_ca+2'][5])

im13 = ax[13].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['X_mg+2'][0])
im13 = ax[13].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['X_mg+2'][1])
im13 = ax[13].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['X_mg+2'][2])
im13 = ax[13].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['X_mg+2'][3])
im13 = ax[13].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['X_mg+2'][4])
im13 = ax[13].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['X_mg+2'][5])

im14 = ax[14].plot(aqui_con.tx_mtx['X'][0],aqui_con.tx_mtx['X_h+'][0])
im14 = ax[14].plot(aqui_con.tx_mtx['X'][1],aqui_con.tx_mtx['X_h+'][1])
im14 = ax[14].plot(aqui_con.tx_mtx['X'][2],aqui_con.tx_mtx['X_h+'][2])
im14 = ax[14].plot(aqui_con.tx_mtx['X'][3],aqui_con.tx_mtx['X_h+'][3])
im14 = ax[14].plot(aqui_con.tx_mtx['X'][4],aqui_con.tx_mtx['X_h+'][4])
im14 = ax[14].plot(aqui_con.tx_mtx['X'][5],aqui_con.tx_mtx['X_h+'][5])

##aqui_min.element.column_name
##['X', 'Y', 'Z', 'T(C)', 'Porosity', 'Poros_Chg', 'Permx(m^2)', 'Kx/Kx0', 'Permz(m^2)', 'Kz/Kz0', 'calcite']

im15 = ax[15].plot(aqui_min.tx_mtx['X'][0],aqui_min.tx_mtx['calcite'][0])
im15 = ax[15].plot(aqui_min.tx_mtx['X'][1],aqui_min.tx_mtx['calcite'][1])
im15 = ax[15].plot(aqui_min.tx_mtx['X'][2],aqui_min.tx_mtx['calcite'][2])
im15 = ax[15].plot(aqui_min.tx_mtx['X'][3],aqui_min.tx_mtx['calcite'][3])
im15 = ax[15].plot(aqui_min.tx_mtx['X'][4],aqui_min.tx_mtx['calcite'][4])
im15 = ax[15].plot(aqui_min.tx_mtx['X'][5],aqui_min.tx_mtx['calcite'][5])


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


#freq=10

#m1 =np.linspace(opt_min_ay[  'S(liq)'     ], opt_max_ay['S(liq)'      ],freq)
#m2 =np.linspace(opt_min_ay[  'DIFFUS.'    ], opt_max_ay['DIFFUS.'     ],freq)
#m3 =np.linspace(opt_min_ay[  'PCAP'       ], opt_max_ay['PCAP'        ],freq)
#m4 =np.linspace(gas_min_ay[  'Sg'         ], gas_max_ay[ 'Sg'         ],freq)
#m5 =np.linspace(gas_min_ay[  'o2(g)'      ], gas_max_ay[ 'o2(g)'      ],freq)
#m6 =np.linspace(sod_min_ay[ 'Porosity'    ], sod_max_ay['Porosity'    ],freq)
#m7 =np.linspace(sod_min_ay[ 'Poros_Chg'   ], sod_max_ay['Poros_Chg'   ],freq)
#m8 =np.linspace(sod_min_ay[ 'Permx(m^2)'  ], sod_max_ay['Permx(m^2)'  ],freq)
#m9 =np.linspace(sod_min_ay[ 'Kx/Kx0'      ], sod_max_ay['Kx/Kx0'      ],freq)
#m10=np.linspace(sod_min_ay[ 'Permz(m^2)'  ], sod_max_ay['Permz(m^2)'  ],freq)
#m11=np.linspace(sod_min_ay[ 'Kz/Kz0'      ], sod_max_ay['Kz/Kz0'      ],freq)
#m12=np.linspace(sod_min_ay[ 'pyrite'      ], sod_max_ay['pyrite'      ],freq)
#m13=np.linspace(sod_min_ay[ 'chalcopyrit' ], sod_max_ay['chalcopyrit' ],freq)
#m14=np.linspace(sod_min_ay[ 'magnetite'   ], sod_max_ay['magnetite'   ],freq)
#m15=np.linspace(sod_min_ay[ 'k-feldspar'  ], sod_max_ay['k-feldspar'  ],freq)
#m16=np.linspace(sod_min_ay[ 'albite'      ], sod_max_ay['albite'      ],freq)
#m17=np.linspace(sod_min_ay[ 'anorthite'   ], sod_max_ay['anorthite'   ],freq)
#m18=np.linspace(sod_min_ay[ 'annite'      ], sod_max_ay['annite'      ],freq)
#m19=np.linspace(sod_min_ay[ 'muscovite'   ], sod_max_ay['muscovite'   ],freq)
#m20=np.linspace(sod_min_ay[ 'anhydrite'   ], sod_max_ay['anhydrite'   ],freq)
#m21=np.linspace(sod_min_ay[ 'goethite'    ], sod_max_ay['goethite'    ],freq)
#m22=np.linspace(sod_min_ay[ 'chalcocite'  ], sod_max_ay['chalcocite'  ],freq)
#m23=np.linspace(sod_min_ay[ 'covellite'   ], sod_max_ay['covellite'   ],freq)
#m24=np.linspace(sod_min_ay[ 'kaolinite'   ], sod_max_ay['kaolinite'   ],freq)
#m25=np.linspace(sod_min_ay[ 'sio2(am)'    ], sod_max_ay['sio2(am)'    ],freq)
#m26=np.linspace(sod_min_ay[ 'alunite'     ], sod_max_ay['alunite'     ],freq)
#m30=np.linspace(aqu_min_ay['t_so4-2'      ], aqu_max_ay['t_so4-2'     ],freq)
#m31=np.linspace(aqu_min_ay['t_fe+2'       ], aqu_max_ay['t_fe+2'      ],freq)
#m32=np.linspace(aqu_min_ay['t_cu+2'       ], aqu_max_ay['t_cu+2'      ],freq)
#m33=np.linspace(aqu_min_ay['t_na+'        ], aqu_max_ay['t_na+'       ],freq)
#m34=np.linspace(aqu_min_ay['t_k+'         ], aqu_max_ay['t_k+'        ],freq)
#m35=np.linspace(aqu_min_ay['t_ca+2'       ], aqu_max_ay['t_ca+2'      ],freq)
#m36=np.linspace(aqu_min_ay['t_alo2-'      ], aqu_max_ay['t_alo2-'     ],freq)
#m37=np.linspace(aqu_min_ay['t_sio2(aq)'   ], aqu_max_ay['t_sio2(aq)'  ],freq)
#m38=np.linspace(aqu_min_ay['P(bar)'       ], aqu_max_ay['P(bar)'      ],freq)
#m39=np.linspace(aqu_min_ay['Sg'           ], aqu_max_ay['Sg'          ],freq)
#m40=np.linspace(aqu_min_ay['Sl'           ], aqu_max_ay['Sl'          ],freq)
#m41=np.linspace(aqu_min_ay['T(C)'         ], aqu_max_ay['T(C)'        ],freq)
#m42=np.linspace(aqu_min_ay['aH2O'         ], aqu_max_ay['aH2O'        ],freq)
#m43=np.linspace(aqu_min_ay['pH'           ], aqu_max_ay['pH'          ],freq)
#m45=np.linspace(aqu_min_ay['t_cl-'        ], aqu_max_ay['t_cl-'       ],freq)



#im1 = ax[1 ].contourf(x_ay , y_mtx , sat_liquid_mtx     ,m1 )
#im2 = ax[2 ].contourf(x_ay , y_mtx , diffus_mtx         ,m2 )
#im3 = ax[3 ].contourf(x_ay , y_mtx , pcap_mtx           ,m3 )
#im4 = ax[4 ].contourf(x_ay , y_mtx , sg_mtx             ,m4 )
#im5 = ax[5 ].contourf(x_ay , y_mtx , o2_mtx             ,m5 )
#im6 = ax[6 ].contourf(x_ay , y_mtx , por_mtx            ,m6 )
#im7 = ax[7 ].contourf(x_ay , y_mtx , poros_chg_mtx      ,m7 )
#im8 = ax[8 ].contourf(x_ay , y_mtx , permx_m2_mtx       ,m8 )
#im9 = ax[9 ].contourf(x_ay , y_mtx , KxPKx0_mtx             )
#im10= ax[10].contourf(x_ay , y_mtx , Permz_m2_mtx       ,m10)
#im11= ax[11].contourf(x_ay , y_mtx , KzPKz0_mtx         )
#im12= ax[12].contourf(x_ay , y_mtx , pyrite_mtx         ,m12)
#im13= ax[13].contourf(x_ay , y_mtx , chalcopyrit_mtx    ,m13)
#im14= ax[14].contourf(x_ay , y_mtx , magnetite_mtx      ,m14)
#im15= ax[15].contourf(x_ay , y_mtx , k_feldspar_mtx     ,m15)
#im16= ax[16].contourf(x_ay , y_mtx , albite_mtx         ,m16)
#im17= ax[17].contourf(x_ay , y_mtx , anorthite_mtx      ,m17)
#im18= ax[18].contourf(x_ay , y_mtx , annite_mtx         ,m18)
#im19= ax[19].contourf(x_ay , y_mtx , muscovite_mtx      ,m19)
#im20= ax[20].contourf(x_ay , y_mtx , anhydrite_mtx      ,m20)
#im21= ax[21].contourf(x_ay , y_mtx , goethite_mtx       ,m21)
#im22= ax[22].contourf(x_ay , y_mtx , chalcocite_mtx     ,m22)
#im23= ax[23].contourf(x_ay , y_mtx , covellite_mtx      ,m23)
#im24= ax[24].contourf(x_ay , y_mtx , kaolinite_mtx      ,m24)
#im25= ax[25].contourf(x_ay , y_mtx , sio2_am_mtx        ,m25)
#im26= ax[26].contourf(x_ay , y_mtx , alunite_mtx        ,m26)
#im30= ax[30].contourf(x_ay , y_mtx , aqu_t_so4_n2_mtx   ,m30) 
#im31= ax[31].contourf(x_ay , y_mtx , aqu_t_fe_p2_mtx    ,m31)
#im32= ax[32].contourf(x_ay , y_mtx , aqu_t_cu_p2_mtx    ,m32)
#im33= ax[33].contourf(x_ay , y_mtx , aqu_t_na_p1_mtx    ,m33)
#im34= ax[34].contourf(x_ay , y_mtx , aqu_t_k_p1_mtx     ,m34)
#im35= ax[35].contourf(x_ay , y_mtx , aqu_t_ca_p2_mtx    ,m35)
#im36= ax[36].contourf(x_ay , y_mtx , aqu_t_alo2_n1_mtx  ,m36)
#im37= ax[37].contourf(x_ay , y_mtx , aqu_t_sio2_aq_mtx  ,m37)
#im38= ax[38].contourf(x_ay , y_mtx , aqu_p_bar_mtx      ,m38)
#im39= ax[39].contourf(x_ay , y_mtx , aqu_sg_mtx         ,m39)
#im40= ax[40].contourf(x_ay , y_mtx , aqu_sl_mtx         ,m40)
#im41= ax[41].contourf(x_ay , y_mtx , aqu_t_c_mtx        )
#im42= ax[42].contourf(x_ay , y_mtx , aqu_ah2o_mtx       ,m42)
#im43= ax[43].contourf(x_ay , y_mtx , aqu_ph_mtx         ,m43)
#im45= ax[45].contourf(x_ay , y_mtx , aqu_t_cl_n1        ,m45)
#im27= ax[27].plot(flow_first_column_ay['FLO(LIQ.)'],y_mtx[1:,0]  )
#im28= ax[28].plot(flow_first_column_ay['VEL(LIQ.)'],y_mtx[1:,0] )
#im29= ax[29].plot(sat_liquid_mtx[:,0], y_mtx[:,0]  )




##  a confirmation flow_first_column_ay['FLO(LIQ.)']/sat_liquid_mtx[:-1,0]/flow_first_column_ay['VEL(LIQ.)'] 
## essentially 
## FLO(LIQ.) [kg/s] = por * sat * VEL(LIQ.) [m3/s]  * density   [kg/m3]  
## the unit of FLO(LIQ.) can be confirmated by the lower value as -5e-7 [kg/s], same as the input in GENER.
#    



##fig.colorbar(im44, ax=ax[44], format='%.1e')
##fig.colorbar(im27, ax=ax[27])
##fig.colorbar(im28, ax=ax[28])
##fig.colorbar(im29, ax=ax[29])
ax[0 ].set_title('aqui_con_\n pH'     ,fontweight='bold')
ax[1 ].set_title('aqui_con_\n t_h20'  ,fontweight='bold')
ax[2 ].set_title('aqui_con_\n t_h+'   ,fontweight='bold')
ax[3 ].set_title('aqui_con_\n t_ca+2' ,fontweight='bold')
ax[4 ].set_title('aqui_con_\n t_mg+2' ,fontweight='bold')
ax[5 ].set_title('aqui_con_\n t_na+'  ,fontweight='bold')
ax[6 ].set_title('aqui_con_\n t_k+'   ,fontweight='bold')
ax[7 ].set_title('aqui_con_\n t_hco3-',fontweight='bold')
ax[8 ].set_title('aqui_con_\n t_so4-2',fontweight='bold')
ax[9 ].set_title('aqui_con_\n t_cl-'  ,fontweight='bold')
ax[10].set_title('aqui_con_\n X_na+'  ,fontweight='bold')
ax[11].set_title('aqui_con_\n X_k+'   ,fontweight='bold')
ax[12].set_title('aqui_con_\n X_ca+2' ,fontweight='bold')
ax[13].set_title('aqui_con_\n X_mg+2' ,fontweight='bold')
ax[14].set_title('aqui_con_\n X_h+'   ,fontweight='bold')
ax[15].set_title('aqui_min_\n calcite',fontweight='bold')

##ax[1].set_title('Saturation',x=0.04,y=0.8,fontweight='bold')
#ax[1 ].set_title('flow.out \n Liquid Saturation' , fontweight='bold')
#ax[2 ].set_title('flow.out \n Diffus'            , fontweight='bold')
#ax[3 ].set_title('flow.out \n Cap. Pre.'         , fontweight='bold')
#ax[4 ].set_title('aqui_gas \n Gas Saturation'    , fontweight='bold')
#ax[5 ].set_title('aqui_gas \n Oxygen'            , fontweight='bold')
#ax[6 ].set_title('aqui_min \n Porosity'          , fontweight='bold')
#ax[7 ].set_title('aqui_min \n Porosity change'   , fontweight='bold')
#ax[8 ].set_title('aqui_min \n Permeability (m2)' , fontweight='bold')
#ax[9 ].set_title('aqui_min \n Kx/Kx0'      , fontweight='bold')
#ax[10].set_title('aqui_min \n Permz(m^2)'  , fontweight='bold')
#ax[11].set_title('aqui_min \n Kz/Kz0'      , fontweight='bold')
#ax[12].set_title('aqui_min \n pyrite'      , fontweight='bold')
#ax[13].set_title('aqui_min \n chalcopyrit' , fontweight='bold')
#ax[14].set_title('aqui_min \n magnetite'   , fontweight='bold')
#ax[15].set_title('aqui_min \n k-feldspar'  , fontweight='bold')
#ax[16].set_title('aqui_min \n albite'      , fontweight='bold')
#ax[17].set_title('aqui_min \n anorthite'   , fontweight='bold')
#ax[18].set_title('aqui_min \n annite'      , fontweight='bold')
#ax[19].set_title('aqui_min \n muscovite'   , fontweight='bold')
#ax[20].set_title('aqui_min \n anhydrite'   , fontweight='bold')
#ax[21].set_title('aqui_min \n goethite'    , fontweight='bold')
#ax[22].set_title('aqui_min \n chalcocite'  , fontweight='bold')
#ax[23].set_title('aqui_min \n covellite'   , fontweight='bold')
#ax[24].set_title('aqui_min \n kaolinite'   , fontweight='bold')
#ax[25].set_title('aqui_min \n sio2(am)'    , fontweight='bold')
#ax[26].set_title('aqui_min \n alunite'     , fontweight='bold')
#
#ax[27].set_title('flow.out \n FLO(LIQ.)_fra(kg/s)'     , fontweight='bold')
#ax[28].set_title('flow.out \n VEL(LIQ.)_fra(m3/s)'     , fontweight='bold')
#ax[29].set_title('flow.out \n sat_liq_fra'     , fontweight='bold')

#ax[30].set_title('aqui_con \n t_so4-2'    ,  fontweight='bold') 
#ax[31].set_title('aqui_con \n t_fe+2'     ,  fontweight='bold') 
#ax[32].set_title('aqui_con \n t_cu+2'     ,  fontweight='bold') 
#ax[33].set_title('aqui_con \n t_na+'      ,  fontweight='bold') 
#ax[34].set_title('aqui_con \n t_k+'       ,  fontweight='bold') 
#ax[35].set_title('aqui_con \n t_ca+2'     ,  fontweight='bold') 
#ax[36].set_title('aqui_con \n t_alo2-'    ,  fontweight='bold') 
#ax[37].set_title('aqui_con \n t_sio2(aq)' ,  fontweight='bold') 
#ax[38].set_title('aqui_con \n P(bar)'     ,  fontweight='bold') 
#ax[39].set_title('aqui_con \n Sg'         ,  fontweight='bold') 
#ax[40].set_title('aqui_con \n Sl'         ,  fontweight='bold') 
#ax[41].set_title('aqui_con \n T(C)'       ,  fontweight='bold') 
#ax[42].set_title('aqui_con \n aH2O'       ,  fontweight='bold') 
#ax[43].set_title('aqui_con \n pH'         ,  fontweight='bold') 
##ax[44].set_title('aqui_con \n ',  fontweight='bold') 
#ax[45].set_title('aqui_con \n t_cl-'      ,  fontweight='bold') 

output_name = 'figure/'+'all'+'.jpg'
fig.savefig(output_name, format='jpg', dpi=100)

#for i in np.arange(plot_every):
#    opt.next()
#    aqui_gas.next()
#    aqui_min.next()
#    aqui_con.next()
    


