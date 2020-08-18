import os # this script plots the output times.  #for ii in opt.times[-1]: 
import pandas as pd
if not os.path.exists('figure'):
        os.makedirs('figure')
#reshape_format=[11,7]
#y_mtx=aqu.element.DataFrame['Y'][1:].values.reshape(reshape_format)
plt.rcParams["axes.labelweight"] = "bold"
x_ay=aqu.element.DataFrame['X'].values
y_ay=aqu.element.DataFrame['Y'].values

opt.first(); gas.first(); aqu.first(); sod.first()



gas.first(); sod.first(); aqu.first()
#for ii in opt.times[0::plot_every]:

fig = plt.figure(figsize=(16,12))
   
tlt =('opt.time='  "%0.2f" % (opt.time/86400/365)   +' years' 
    + ', sod.time='  "%0.2f" % (sod.time   ) +' years'
    ', aqu.time='  "%0.2f" % (aqu.time   ) +' years'
    ', aqu.time='  "%0.2f" % (gas.time   ) +' years')
#fig.suptitle(   tlt     , fontsize=16,fontweight="bold")
print(tlt)
no_row=7
no_col=5
ax = [[] for i in range(no_row*no_col)]

k=0
for i in np.arange(no_row):
    for j in np.arange(no_col):
        ax[k]= plt.subplot2grid((no_row, no_col), (i, j), colspan=1)
        ax[k].xaxis.set_tick_params(labelsize=6)
        ax[k].yaxis.set_tick_params(labelsize=6)
        
        k+=1
        
def plot_mineral_profile(ax_idx=ax[15], mineral_name='siderite',sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx ):
    if any(mineral_name == s for s in sod_input.element.column_name):
        i = opt_idx[0] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
        i = opt_idx[1] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
        i = opt_idx[2] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
        i = opt_idx[3] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
        i = opt_idx[4] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)
        i = opt_idx[5] ; im15 = ax_idx.plot(sod_input.tx_mtx[mineral_name][i] , ele_depth_m)

        ax_idx.set_xlabel('sod_'+ mineral_name ,fontweight='bold',fontsize=8)
        ax_idx.invert_yaxis()
        ax_idx.set_ylabel('Depth (m)' , fontweight='bold')


def plot_aqua_profile(ax_idx=ax[25], aqu_name='t_sio2(aq)',aqu_input=aqu,ele_depth_m=ele_depth_m,opt_idx=opt_idx ):
    if any("t_sio2(aq)" in s for s in aqu.element.column_name):
        i = opt_idx[0] ; im25 = ax_idx.plot( aqu_input.tx_mtx[aqu_name][i] , ele_depth_m )
        i = opt_idx[1] ; im25 = ax_idx.plot( aqu_input.tx_mtx[aqu_name][i] , ele_depth_m )
        i = opt_idx[2] ; im25 = ax_idx.plot( aqu_input.tx_mtx[aqu_name][i] , ele_depth_m )
        i = opt_idx[3] ; im25 = ax_idx.plot( aqu_input.tx_mtx[aqu_name][i] , ele_depth_m )
        i = opt_idx[4] ; im25 = ax_idx.plot( aqu_input.tx_mtx[aqu_name][i] , ele_depth_m )
        i = opt_idx[5] ; im25 = ax_idx.plot( aqu_input.tx_mtx[aqu_name][i] , ele_depth_m )
        ax_idx.set_xlabel('aqu_'+ aqu_name ,fontweight='bold',fontsize=8)
        ax_idx.invert_yaxis()
        ax_idx.set_ylabel('Depth (m)' , fontweight='bold',fontsize=8)




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



if any("t_alo2-" in s for s in aqu.element.column_name):
    i = opt_idx[0] ; im3 = ax[3].plot( aqu.tx_mtx['t_alo2-'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
    i = opt_idx[1] ; im3 = ax[3].plot( aqu.tx_mtx['t_alo2-'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
    i = opt_idx[2] ; im3 = ax[3].plot( aqu.tx_mtx['t_alo2-'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
    i = opt_idx[3] ; im3 = ax[3].plot( aqu.tx_mtx['t_alo2-'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
    i = opt_idx[4] ; im3 = ax[3].plot( aqu.tx_mtx['t_alo2-'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
    i = opt_idx[5] ; im3 = ax[3].plot( aqu.tx_mtx['t_alo2-'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
#im3 = ax[3].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['pH']['ctot'] )


i = opt_idx[0] ; im4 = ax[4].plot(aqu.tx_mtx['t_o2(aq)'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[1] ; im4 = ax[4].plot(aqu.tx_mtx['t_o2(aq)'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[2] ; im4 = ax[4].plot(aqu.tx_mtx['t_o2(aq)'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[3] ; im4 = ax[4].plot(aqu.tx_mtx['t_o2(aq)'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[4] ; im4 = ax[4].plot(aqu.tx_mtx['t_o2(aq)'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
i = opt_idx[5] ; im4 = ax[4].plot(aqu.tx_mtx['t_o2(aq)'][i] , ele_depth_m ,label="%.1e" % aqu.times[i]+'yrs')
#im4 = ax[4].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['mg+2']['ctot'] )
ax[4].legend(bbox_to_anchor=(1.02, 1.), loc=2, borderaxespad=0.)

i = opt_idx[0] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i]*gas.tx_mtx['Sg'][i] , ele_depth_m )
i = opt_idx[1] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i]*gas.tx_mtx['Sg'][i] , ele_depth_m )
i = opt_idx[2] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i]*gas.tx_mtx['Sg'][i] , ele_depth_m )
i = opt_idx[3] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i]*gas.tx_mtx['Sg'][i] , ele_depth_m )
i = opt_idx[4] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i]*gas.tx_mtx['Sg'][i] , ele_depth_m )
i = opt_idx[5] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i]*gas.tx_mtx['Sg'][i] , ele_depth_m )
#i = opt_idx[0] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i], ele_depth_m )
#i = opt_idx[1] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i], ele_depth_m )
#i = opt_idx[2] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i], ele_depth_m )
#i = opt_idx[3] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i], ele_depth_m )
#i = opt_idx[4] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i], ele_depth_m )
#i = opt_idx[5] ;im5 = ax[5].plot( gas.tx_mtx['o2(g)'][i], ele_depth_m )
#im5 = ax[5].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['na+']['ctot'] )
#
i = opt_idx[0] ; im6 = ax[6].plot(aqu.tx_mtx['Sg'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m )
i = opt_idx[1] ; im6 = ax[6].plot(aqu.tx_mtx['Sg'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m )
i = opt_idx[2] ; im6 = ax[6].plot(aqu.tx_mtx['Sg'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m )
i = opt_idx[3] ; im6 = ax[6].plot(aqu.tx_mtx['Sg'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m )
i = opt_idx[4] ; im6 = ax[6].plot(aqu.tx_mtx['Sg'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m )
i = opt_idx[5] ; im6 = ax[6].plot(aqu.tx_mtx['Sg'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m )

i = opt_idx[0] ; im6 = ax[6].plot(aqu.tx_mtx['Sl'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m, ':' )
i = opt_idx[1] ; im6 = ax[6].plot(aqu.tx_mtx['Sl'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m, ':' )
i = opt_idx[2] ; im6 = ax[6].plot(aqu.tx_mtx['Sl'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m, ':' )
i = opt_idx[3] ; im6 = ax[6].plot(aqu.tx_mtx['Sl'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m, ':' )
i = opt_idx[4] ; im6 = ax[6].plot(aqu.tx_mtx['Sl'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m, ':' )
i = opt_idx[5] ; im6 = ax[6].plot(aqu.tx_mtx['Sl'][i]*sod.tx_mtx['Porosity'][i] , ele_depth_m, ':' )

#im6 = ax[6].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['k+']['ctot'] )
#
if any("t_fe+2" in s for s in aqu.element.column_name):
    i = opt_idx[0] ; im7 = ax[7].plot( aqu.tx_mtx['t_fe+2'][i] , ele_depth_m )
    i = opt_idx[1] ; im7 = ax[7].plot( aqu.tx_mtx['t_fe+2'][i] , ele_depth_m )
    i = opt_idx[2] ; im7 = ax[7].plot( aqu.tx_mtx['t_fe+2'][i] , ele_depth_m )
    i = opt_idx[3] ; im7 = ax[7].plot( aqu.tx_mtx['t_fe+2'][i] , ele_depth_m )
    i = opt_idx[4] ; im7 = ax[7].plot( aqu.tx_mtx['t_fe+2'][i] , ele_depth_m )
    i = opt_idx[5] ; im7 = ax[7].plot( aqu.tx_mtx['t_fe+2'][i] , ele_depth_m )
#im7 = ax[7].plot(aqu.tx_mtx['X'][0] , aqu.tx_mtx['t_hco3-'][0])
#im7 = ax[7].plot(aqu.tx_mtx['X'][1] , aqu.tx_mtx['t_hco3-'][1])
#im7 = ax[7].plot(aqu.tx_mtx['X'][2] , aqu.tx_mtx['t_hco3-'][2])
#im7 = ax[7].plot(aqu.tx_mtx['X'][3] , aqu.tx_mtx['t_hco3-'][3])
#im7 = ax[7].plot(aqu.tx_mtx['X'][4] , aqu.tx_mtx['t_hco3-'][4])
#im7 = ax[7].plot(aqu.tx_mtx['X'][5] , aqu.tx_mtx['t_hco3-'][5])
#im7 = ax[7].scatter(aqu.tx_mtx['X'][0][0],
#        chem_inp.water['list']['boundary']['1']['hco3-']['ctot'] )

if any("t_so4-2" in s for s in aqu.element.column_name):
    i = opt_idx[0] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
    i = opt_idx[1] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
    i = opt_idx[2] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
    i = opt_idx[3] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
    i = opt_idx[4] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )
    i = opt_idx[5] ; im8 = ax[8].plot( aqu.tx_mtx['t_so4-2'][i] , ele_depth_m )


#if any("t_ca+2" in s for s in aqu.element.column_name):
#    i = opt_idx[0] ; im9 = ax[9].plot( aqu.tx_mtx['t_ca+2'][i] , ele_depth_m )
#    i = opt_idx[1] ; im9 = ax[9].plot( aqu.tx_mtx['t_ca+2'][i] , ele_depth_m )
#    i = opt_idx[2] ; im9 = ax[9].plot( aqu.tx_mtx['t_ca+2'][i] , ele_depth_m )
#    i = opt_idx[3] ; im9 = ax[9].plot( aqu.tx_mtx['t_ca+2'][i] , ele_depth_m )
#    i = opt_idx[4] ; im9 = ax[9].plot( aqu.tx_mtx['t_ca+2'][i] , ele_depth_m )
#    i = opt_idx[5] ; im9 = ax[9].plot( aqu.tx_mtx['t_ca+2'][i] , ele_depth_m )

#if any("t_hco3-" in s for s in aqu.element.column_name):
#    i = opt_idx[0] ; im10 = ax[10].plot( aqu.tx_mtx['t_hco3-'][i] , ele_depth_m )
#    i = opt_idx[1] ; im10 = ax[10].plot( aqu.tx_mtx['t_hco3-'][i] , ele_depth_m )
#    i = opt_idx[2] ; im10 = ax[10].plot( aqu.tx_mtx['t_hco3-'][i] , ele_depth_m )
#    i = opt_idx[3] ; im10 = ax[10].plot( aqu.tx_mtx['t_hco3-'][i] , ele_depth_m )
#    i = opt_idx[4] ; im10 = ax[10].plot( aqu.tx_mtx['t_hco3-'][i] , ele_depth_m )
#    i = opt_idx[5] ; im10 = ax[10].plot( aqu.tx_mtx['t_hco3-'][i] , ele_depth_m )


##sod.element.column_name
##['X', 'Y', 'Z', 'T(C)', 'Porosity', 'Poros_Chg', 'Permx(m^2)', 'Kx/Kx0', 'Permz(m^2)', 'Kz/Kz0', 'calcite']
#if any("chlorite" in s for s in sod.element.column_name):
#    i = opt_idx[0] ; im11 = ax[11].plot(sod.tx_mtx['chlorite'][i] , ele_depth_m)
#    i = opt_idx[1] ; im11 = ax[11].plot(sod.tx_mtx['chlorite'][i] , ele_depth_m)
#    i = opt_idx[2] ; im11 = ax[11].plot(sod.tx_mtx['chlorite'][i] , ele_depth_m)
#    i = opt_idx[3] ; im11 = ax[11].plot(sod.tx_mtx['chlorite'][i] , ele_depth_m)
#    i = opt_idx[4] ; im11 = ax[11].plot(sod.tx_mtx['chlorite'][i] , ele_depth_m)
#    i = opt_idx[5] ; im11 = ax[11].plot(sod.tx_mtx['chlorite'][i] , ele_depth_m)

#if any("dolomite" in s for s in sod.element.column_name):
#    i = opt_idx[0] ; im12 = ax[12].plot(sod.tx_mtx['dolomite'][i] , ele_depth_m)
#    i = opt_idx[1] ; im12 = ax[12].plot(sod.tx_mtx['dolomite'][i] , ele_depth_m)
#    i = opt_idx[2] ; im12 = ax[12].plot(sod.tx_mtx['dolomite'][i] , ele_depth_m)
#    i = opt_idx[3] ; im12 = ax[12].plot(sod.tx_mtx['dolomite'][i] , ele_depth_m)
#    i = opt_idx[4] ; im12 = ax[12].plot(sod.tx_mtx['dolomite'][i] , ele_depth_m)
#    i = opt_idx[5] ; im12 = ax[12].plot(sod.tx_mtx['dolomite'][i] , ele_depth_m)

#if any("calcite" in s for s in sod.element.column_name):
#    i = opt_idx[0] ; im13 = ax[13].plot(sod.tx_mtx['calcite'][i] , ele_depth_m)
#    i = opt_idx[1] ; im13 = ax[13].plot(sod.tx_mtx['calcite'][i] , ele_depth_m)
#    i = opt_idx[2] ; im13 = ax[13].plot(sod.tx_mtx['calcite'][i] , ele_depth_m)
#    i = opt_idx[3] ; im13 = ax[13].plot(sod.tx_mtx['calcite'][i] , ele_depth_m)
#    i = opt_idx[4] ; im13 = ax[13].plot(sod.tx_mtx['calcite'][i] , ele_depth_m)
#    i = opt_idx[5] ; im13 = ax[13].plot(sod.tx_mtx['calcite'][i] , ele_depth_m)

#if any("gypsum" in s for s in sod.element.column_name):
#    i = opt_idx[0] ; im14 = ax[14].plot(sod.tx_mtx['gypsum'][i] , ele_depth_m)
#    i = opt_idx[1] ; im14 = ax[14].plot(sod.tx_mtx['gypsum'][i] , ele_depth_m)
#    i = opt_idx[2] ; im14 = ax[14].plot(sod.tx_mtx['gypsum'][i] , ele_depth_m)
#    i = opt_idx[3] ; im14 = ax[14].plot(sod.tx_mtx['gypsum'][i] , ele_depth_m)
#    i = opt_idx[4] ; im14 = ax[14].plot(sod.tx_mtx['gypsum'][i] , ele_depth_m)
#    i = opt_idx[5] ; im14 = ax[14].plot(sod.tx_mtx['gypsum'][i] , ele_depth_m)


#if any("pyrite" in s for s in sod.element.column_name):
#    i = opt_idx[0] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
#    i = opt_idx[1] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
#    i = opt_idx[2] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
#    i = opt_idx[3] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
#    i = opt_idx[4] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)
#    i = opt_idx[5] ; im15 = ax[15].plot(sod.tx_mtx['pyrite'][i] , ele_depth_m)

#list(opt.tx_con_mtx)
#['FLOH', 'FLOH/FLOF', 'FLOF', 'FLO(GAS)', 'VAPDIF', 'FLO(LIQ.)', 'VEL(GAS)', 'VEL(LIQ.)']

i = opt_idx[0] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i]*sPday/liquid_density_kgPm3/dx[0]/dy[0]/mPmm, con_depth_m)
i = opt_idx[1] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i]*sPday/liquid_density_kgPm3/dx[0]/dy[0]/mPmm, con_depth_m)
i = opt_idx[2] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i]*sPday/liquid_density_kgPm3/dx[0]/dy[0]/mPmm, con_depth_m)
i = opt_idx[3] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i]*sPday/liquid_density_kgPm3/dx[0]/dy[0]/mPmm, con_depth_m)
i = opt_idx[4] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i]*sPday/liquid_density_kgPm3/dx[0]/dy[0]/mPmm, con_depth_m)
i = opt_idx[5] ; im16 = ax[16].plot(opt.tx_con_mtx['FLO(LIQ.)'][i]*sPday/liquid_density_kgPm3/dx[0]/dy[0]/mPmm, con_depth_m)

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


im20 = ax[20].plot( aqu.times,aqu.tx_mtx['pH'][:,-2],'-',label='Simulation' )
im20 = ax[20].plot(field_data['pH']['years'],field_data['pH'][1],':o',label='Col. 1',color='blue'  )
im20 = ax[20].plot(field_data['pH']['years'],field_data['pH'][2],':o',label='Col. 2',color='red'   )
im20 = ax[20].plot(field_data['pH']['years'],field_data['pH'][3],':o',label='Col. 3',color='green' )
im20 = ax[20].plot(field_data['pH']['years'],field_data['pH'][3],':o',label='Col. 4',color='purple')
im20 = ax[20].plot(field_data['pH']['years'],field_data['pH'][4],':o',label='Col. 5',color='cyan'  )
im20 = ax[20].plot(field_data['pH']['years'],field_data['pH'][5],':o',label='Col. 6',color='orange')


if any("t_so4-2" in s for s in aqu.element.column_name):
    im21 = ax[21].plot( aqu.times,aqu.tx_mtx['t_so4-2'][:,-2] * mmass_sulphate_kgPmol* mgPkg,'-',label='Simulation' )

im21 = ax[21].plot(field_data['col1'].loc['years'],field_data['col1'].loc['Sulphate'] , ':o',label='Col 1',color='blue'  )
im21 = ax[21].plot(field_data['col2'].loc['years'],field_data['col2'].loc['Sulphate'] , ':o',label='Col 2',color='red'   )
im21 = ax[21].plot(field_data['col3'].loc['years'],field_data['col3'].loc['Sulphate'] , ':o',label='Col 3',color='green' )
im21 = ax[21].plot(field_data['col4'].loc['years'],field_data['col4'].loc['Sulphate'] , ':o',label='Col 4',color='purple')
im21 = ax[21].plot(field_data['col5'].loc['years'],field_data['col5'].loc['Sulphate'] , ':o',label='Col 5',color='cyan'  )
im21 = ax[21].plot(field_data['col6'].loc['years'],field_data['col6'].loc['Sulphate'] , ':o',label='Col 6',color='orange')


if any("t_fe+2" in s for s in aqu.element.column_name):
    im21 = ax[22].plot( aqu.times,aqu.tx_mtx['t_fe+2'][:,-2] * mmass_iron2_kgPmol* mgPkg,'-',label='Simulation' )
im22 = ax[22].plot(field_data['col1'].loc['years'],field_data['col1'].loc['Fe Total'] , ':o',label='Col 1',color='blue'  )
im22 = ax[22].plot(field_data['col2'].loc['years'],field_data['col2'].loc['Fe Total'] , ':o',label='Col 2',color='red'   )
im22 = ax[22].plot(field_data['col3'].loc['years'],field_data['col3'].loc['Fe Total'] , ':o',label='Col 3',color='green' )
im22 = ax[22].plot(field_data['col4'].loc['years'],field_data['col4'].loc['Fe Total'] , ':o',label='Col 4',color='purple')
im22 = ax[22].plot(field_data['col5'].loc['years'],field_data['col5'].loc['Fe Total'] , ':o',label='Col 5',color='cyan'  )
im22 = ax[22].plot(field_data['col6'].loc['years'],field_data['col6'].loc['Fe Total'] , ':o',label='Col 6',color='orange')

if any("t_ca+2" in s for s in aqu.element.column_name):
    im23 = ax[23].plot( aqu.times,aqu.tx_mtx['t_ca+2'][:,-2] * mmass_ca_kgPmol* mgPkg,'-',label='Simulation' )
im23 = ax[23].plot(field_data['col1'].loc['years'],field_data['col1'].loc['Ca Total'] , ':o',label='Col 1' , color='blue'  )
im23 = ax[23].plot(field_data['col2'].loc['years'],field_data['col2'].loc['Ca Total'] , ':o',label='Col 2' , color='red'   )
im23 = ax[23].plot(field_data['col3'].loc['years'],field_data['col3'].loc['Ca Total'] , ':o',label='Col 3' , color='green' )
im23 = ax[23].plot(field_data['col4'].loc['years'],field_data['col4'].loc['Ca Total'] , ':o',label='Col 4' , color='purple')
im23 = ax[23].plot(field_data['col5'].loc['years'],field_data['col5'].loc['Ca Total'] , ':o',label='Col 5' , color='cyan'  )
im23 = ax[23].plot(field_data['col6'].loc['years'],field_data['col6'].loc['Ca Total'] , ':o',label='Col 6' , color='orange')

if any("t_mg+2" in s for s in aqu.element.column_name):
    im24 = ax[24].plot( aqu.times,aqu.tx_mtx['t_mg+2'][:,-2] * mmass_mg_kgPmol* mgPkg,'-',label='Simulation' )
im24 = ax[24].plot(field_data['col1'].loc['years'],field_data['col1'].loc['Mg Total'] , ':o',label='Col 1' , color='blue'  )
im24 = ax[24].plot(field_data['col2'].loc['years'],field_data['col2'].loc['Mg Total'] , ':o',label='Col 2' , color='red'   )
im24 = ax[24].plot(field_data['col3'].loc['years'],field_data['col3'].loc['Mg Total'] , ':o',label='Col 3' , color='green' )
im24 = ax[24].plot(field_data['col4'].loc['years'],field_data['col4'].loc['Mg Total'] , ':o',label='Col 4' , color='purple')
im24 = ax[24].plot(field_data['col5'].loc['years'],field_data['col5'].loc['Mg Total'] , ':o',label='Col 5' , color='cyan'  )
im24 = ax[24].plot(field_data['col6'].loc['years'],field_data['col6'].loc['Mg Total'] , ':o',label='Col 6' , color='orange')
ax[24].legend(bbox_to_anchor=(1.02, 1.), loc=2, borderaxespad=0.)


#if any("t_sio2(aq)" in s for s in aqu.element.column_name):
#    i = opt_idx[0] ; im25 = ax[25].plot( aqu.tx_mtx['t_sio2(aq)'][i] , ele_depth_m )
#    i = opt_idx[1] ; im25 = ax[25].plot( aqu.tx_mtx['t_sio2(aq)'][i] , ele_depth_m )
#    i = opt_idx[2] ; im25 = ax[25].plot( aqu.tx_mtx['t_sio2(aq)'][i] , ele_depth_m )
#    i = opt_idx[3] ; im25 = ax[25].plot( aqu.tx_mtx['t_sio2(aq)'][i] , ele_depth_m )
#    i = opt_idx[4] ; im25 = ax[25].plot( aqu.tx_mtx['t_sio2(aq)'][i] , ele_depth_m )
#    i = opt_idx[5] ; im25 = ax[25].plot( aqu.tx_mtx['t_sio2(aq)'][i] , ele_depth_m )

plot_aqua_profile(ax_idx=ax[ 9], aqu_name='t_ca+2'    ,aqu_input=aqu,ele_depth_m=ele_depth_m,opt_idx=opt_idx )
plot_aqua_profile(ax_idx=ax[10], aqu_name='t_hco3-'    ,aqu_input=aqu,ele_depth_m=ele_depth_m,opt_idx=opt_idx )
#plot_aqua_profile(ax_idx=ax[20], aqu_name='pH'    ,aqu_input=aqu,ele_depth_m=ele_depth_m,opt_idx=opt_idx )
plot_aqua_profile(ax_idx=ax[25], aqu_name='t_sio2(aq)',aqu_input=aqu,ele_depth_m=ele_depth_m,opt_idx=opt_idx )
plot_aqua_profile(ax_idx=ax[33], aqu_name='P(bar)',aqu_input=aqu,ele_depth_m=ele_depth_m,opt_idx=opt_idx )


im26 = ax[26].plot(field_data['col1'].loc['Ca Total'] , field_data['col1'].loc['Sulphate'] , 'o',label='Col 1' , color='blue'  ,markersize=2)
im26 = ax[26].plot(field_data['col2'].loc['Ca Total'] , field_data['col2'].loc['Sulphate'] , 'o',label='Col 2' , color='red'   ,markersize=2)
im26 = ax[26].plot(field_data['col3'].loc['Ca Total'] , field_data['col3'].loc['Sulphate'] , 'o',label='Col 3' , color='green' ,markersize=2)
im26 = ax[26].plot(field_data['col4'].loc['Ca Total'] , field_data['col4'].loc['Sulphate'] , 'o',label='Col 4' , color='purple',markersize=2)
im26 = ax[26].plot(field_data['col5'].loc['Ca Total'] , field_data['col5'].loc['Sulphate'] , 'o',label='Col 5' , color='cyan'  ,markersize=2)
im26 = ax[26].plot(field_data['col6'].loc['Ca Total'] , field_data['col6'].loc['Sulphate'] , 'o',label='Col 6' , color='orange',markersize=2)
ca_ay=np.linspace(ax[26].get_xlim()[0], ax[26].get_xlim()[1],10)
sulphate_ay=ca_ay/mmass_ca_kgPmol*mmass_sulphate_kgPmol 
im26 = ax[26].plot(ca_ay,sulphate_ay, '-',label='CaSo4' , color='orange')
if (any("t_ca+2" in s for s in aqu.element.column_name) and any("t_so4-2" in s for s in aqu.element.column_name)  )  :
    i = opt_idx[1] ; im26 = ax[26].plot( aqu.tx_mtx['t_ca+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_so4-2'][i][::5]*mmass_sulphate_kgPmol*mgPkg , 'x' , markersize=6, color = 'brown')
    i = opt_idx[3] ; im26 = ax[26].plot( aqu.tx_mtx['t_ca+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_so4-2'][i][::5]*mmass_sulphate_kgPmol*mgPkg , '+' , markersize=6, color = 'brown')
    i = opt_idx[5] ; im26 = ax[26].plot( aqu.tx_mtx['t_ca+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_so4-2'][i][::5]*mmass_sulphate_kgPmol*mgPkg , '*' , markersize=6, color = 'brown')


# Mgso4
im27 = ax[27].plot(field_data['col1'].loc['Mg Total'] , field_data['col1'].loc['Sulphate'] , 'o',label = 'Col 1' , color = 'blue'  ,markersize = 2)
im27 = ax[27].plot(field_data['col2'].loc['Mg Total'] , field_data['col2'].loc['Sulphate'] , 'o',label = 'Col 2' , color = 'red'   ,markersize = 2)
im27 = ax[27].plot(field_data['col3'].loc['Mg Total'] , field_data['col3'].loc['Sulphate'] , 'o',label = 'Col 3' , color = 'green' ,markersize = 2)
im27 = ax[27].plot(field_data['col4'].loc['Mg Total'] , field_data['col4'].loc['Sulphate'] , 'o',label = 'Col 4' , color = 'purple',markersize = 2)
im27 = ax[27].plot(field_data['col5'].loc['Mg Total'] , field_data['col5'].loc['Sulphate'] , 'o',label = 'Col 5' , color = 'cyan'  ,markersize = 2)
im27 = ax[27].plot(field_data['col6'].loc['Mg Total'] , field_data['col6'].loc['Sulphate'] , 'o',label = 'Col 6' , color = 'orange',markersize = 2)
mg_ay       = np.linspace(ax[27].get_xlim()[0], ax[27].get_xlim()[1],10)
sulphate_ay = mg_ay/mmass_mg_kgPmol*mmass_sulphate_kgPmol
im27 = ax[27].plot(mg_ay,sulphate_ay, '-',label = 'MgSo4' , color = 'orange')

# caso4
if (any("t_ca+2" in s for s in aqu.element.column_name) and any("t_so4-2" in s for s in aqu.element.column_name)  )  :
    i = opt_idx[1] ; im26 = ax[27].plot( aqu.tx_mtx['t_mg+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_so4-2'][i][::5]*mmass_sulphate_kgPmol*mgPkg , 'x' , markersize=6, color = 'brown')
    i = opt_idx[3] ; im26 = ax[27].plot( aqu.tx_mtx['t_mg+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_so4-2'][i][::5]*mmass_sulphate_kgPmol*mgPkg , '+' , markersize=6, color = 'brown')
    i = opt_idx[5] ; im26 = ax[27].plot( aqu.tx_mtx['t_mg+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_so4-2'][i][::5]*mmass_sulphate_kgPmol*mgPkg , '*' , markersize=6, color = 'brown')


# ca(hco3)2
if (any("t_ca+2" in s for s in aqu.element.column_name) and any("t_hco3-" in s for s in aqu.element.column_name)  )  :
    i = opt_idx[1] ; im26 = ax[28].plot( aqu.tx_mtx['t_ca+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_hco3-'][i][::5]*mmass_sulphate_kgPmol*mgPkg , 'x' , markersize=6, color = 'brown')
    i = opt_idx[3] ; im26 = ax[28].plot( aqu.tx_mtx['t_ca+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_hco3-'][i][::5]*mmass_sulphate_kgPmol*mgPkg , '+' , markersize=6, color = 'brown')
    i = opt_idx[5] ; im26 = ax[28].plot( aqu.tx_mtx['t_ca+2'][i][::5]*mmass_ca_kgPmol*mgPkg , aqu.tx_mtx['t_hco3-'][i][::5]*mmass_sulphate_kgPmol*mgPkg , '*' , markersize=6, color = 'brown')
ca_ay       = np.linspace(ax[28].get_xlim()[0], ax[28].get_xlim()[1],10)
hco3_ay = mg_ay/mmass_ca_kgPmol*mmass_hco3_kgPmol
im28 = ax[28].plot(ca_ay,hco3_ay, '-',label = 'Ca(HCO3)2' , color = 'orange')


plot_mineral_profile(ax_idx=ax[11], mineral_name='chlorite',sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx)
plot_mineral_profile(ax_idx=ax[12], mineral_name='dolomite',sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx)
plot_mineral_profile(ax_idx=ax[13], mineral_name='calcite' ,sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx)
plot_mineral_profile(ax_idx=ax[14], mineral_name='gypsum'  ,sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx)
plot_mineral_profile(ax_idx=ax[15], mineral_name='pyrite'  ,sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx)
plot_mineral_profile(ax_idx=ax[29], mineral_name='siderite',sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx)
plot_mineral_profile(ax_idx=ax[30], mineral_name='magnesite-2',sod_input=sod,ele_depth_m=ele_depth_m,opt_idx=opt_idx)

plt.show(block=False)
#ax[0].scatter(aqu.element.DataFrame['X'],aqu.element.DataFrame['Y'])

# opt.element.column_name
# ['PRES', 'S(liq)', 'PCAP', 'K(rel)', 'DIFFUS.']
# NOTE: capillary pressure is negative in TOUGH


#flow_first_column_ay=opt.connection.DataFrame.loc[mask_first_column_index_ay]

##aqu.element.column_name
##conclusion  aqu_sg_mtx + aqu_sl_mtx  ==1 

##  a confirmation flow_first_column_ay['FLO(LIQ.)']/sat_liquid_mtx[:-1,0]/flow_first_column_ay['VEL(LIQ.)'] 
## essentially 
## FLO(LIQ.) [kg/s] = por * sat * VEL(LIQ.) [m3/s]  * density   [kg/m3]  
## the unit of FLO(LIQ.) can be confirmated by the lower value as -5e-7 [kg/s], same as the input in GENER.
#    



#ax[0 ].set_title('aqu_ pH'     ,fontweight='bold')
#ax[1 ].set_title('aqu_ t_h20'  ,fontweight='bold')
#ax[2 ].set_title('aqu_ t_h+'   ,fontweight='bold')
#ax[3 ].set_title('aqu_ t_ca+2' ,fontweight='bold')
#ax[4 ].set_title('aqu_ t_o2(aq)' ,fontweight='bold')
#ax[5 ].set_title('gas_o2(g)*sg'  ,fontweight='bold')
#ax[6 ].set_title('aqu_ Sg _ Sl'   ,fontweight='bold')
#ax[7 ].set_title('aqu_ t_hco3-',fontweight='bold')
#ax[8 ].set_title('aqu_ t_so4-2',fontweight='bold')
#ax[9 ].set_title('aqu_ t_cl-'  ,fontweight='bold')
#ax[10].set_title('aqu_ X_na+'  ,fontweight='bold')
#ax[11].set_title('aqu_ X_k+'   ,fontweight='bold')
#ax[12].set_title('aqu_ X_ca+2' ,fontweight='bold')
#ax[13].set_title('aqu_ X_mg+2' ,fontweight='bold')
#ax[14].set_title('aqu_ X_h+'   ,fontweight='bold')
#ax[16].set_title('opt_FLO(LIQ)',fontweight='bold')
#ax[17].set_title('opt_VEL(LIQ)',fontweight='bold')
#ax[18].set_title('opt_FLO(GAS)',fontweight='bold')
#ax[19].set_title('opt_VEL(GAS)',fontweight='bold')

ax[0 ].invert_yaxis()
ax[1 ].invert_yaxis()
ax[2 ].invert_yaxis()
ax[3 ].invert_yaxis()
ax[4 ].invert_yaxis()
ax[5 ].invert_yaxis()
ax[6 ].invert_yaxis()
ax[7 ].invert_yaxis()
ax[8 ].invert_yaxis()
ax[16].invert_yaxis()
ax[17].invert_yaxis()
ax[18].invert_yaxis()
ax[19].invert_yaxis()

ax[0 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[1 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[2 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[3 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[4 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[5 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[6 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[7 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[8 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[9 ].set_ylabel('Depth (m)' , fontweight='bold')
ax[10].set_ylabel('Depth (m)' , fontweight='bold')
ax[11].set_ylabel('Depth (m)' , fontweight='bold')
ax[12].set_ylabel('Depth (m)' , fontweight='bold')
ax[13].set_ylabel('Depth (m)' , fontweight='bold')
ax[14].set_ylabel('Depth (m)' , fontweight='bold')
ax[15].set_ylabel('Depth (m)' , fontweight='bold')
ax[16].set_ylabel('Depth (m)' , fontweight='bold')
ax[17].set_ylabel('Depth (m)' , fontweight='bold')
ax[18].set_ylabel('Depth (m)' , fontweight='bold')
ax[19].set_ylabel('Depth (m)' , fontweight='bold')
ax[20].set_ylabel('pH' , fontweight='bold')
ax[21].set_ylabel('t_so4-2 mg/L' , fontweight='bold')
ax[22].set_ylabel('t_fe+2 mg/L' , fontweight='bold')
ax[23].set_ylabel('t_ca+2 mg/L' , fontweight='bold')
ax[24].set_ylabel('t_mg+2 mg/L' , fontweight='bold')
#ax[25].set_ylabel('t_hco3- mg/L' , fontweight='bold')
ax[25].set_ylabel('Depth (m)' , fontweight='bold')
ax[26].set_ylabel('t_ca+2 mg/L' , fontweight='bold')
ax[27].set_ylabel('t_mg+2 mg/L' , fontweight='bold')
ax[28].set_ylabel('t_ca+2 mg/L' , fontweight='bold')

# unit is given from aqu.dat header
ax[0 ].set_xlabel('pH'     ,fontweight='bold')
ax[1 ].set_xlabel('t_h20   mol/L'  ,fontweight='bold')
ax[2 ].set_xlabel('t_h+    mol/L'   ,fontweight='bold')
ax[3 ].set_xlabel('t_alo2- mol/L' ,fontweight='bold')
ax[4 ].set_xlabel('t_o2(aq)mol/L' ,fontweight='bold')
ax[5 ].set_xlabel('gas_o2(g)*sgl'  ,fontweight='bold')
ax[6 ].set_xlabel('Sg_Sl_Porosity'   ,fontweight='bold')
ax[7 ].set_xlabel('t_fe+2 mol/L',fontweight='bold')
ax[8 ].set_xlabel('t_so4-2 mol/L',fontweight='bold')
ax[9 ].set_xlabel('t_ca+2  mol/L',fontweight='bold')
ax[10].set_xlabel('t_hco3- mol/L'  ,fontweight='bold')
ax[11].set_xlabel('sod_chlorite'   ,fontweight='bold')
ax[12].set_xlabel('sod_dolomite' ,fontweight='bold')
ax[13].set_xlabel('sod_calcite' ,fontweight='bold')
ax[14].set_xlabel('sod_gypsum'   ,fontweight='bold')
ax[15].set_xlabel('sod_ pyrite',fontweight='bold')
ax[16].set_xlabel('opt_FLO(LIQ)(mm/day)',fontweight='bold')
ax[17].set_xlabel('opt_VEL(LIQ)',fontweight='bold')
ax[18].set_xlabel('opt_FLO(GAS)(kg/s)',fontweight='bold')
ax[19].set_xlabel('opt_VEL(GAS)',fontweight='bold')
ax[20].set_xlabel('TIME (years)',fontweight='bold')
ax[21].set_xlabel('TIME (years)',fontweight='bold')
ax[22].set_xlabel('TIME (years)',fontweight='bold')
ax[23].set_xlabel('TIME (years)',fontweight='bold')
ax[24].set_xlabel('TIME (years)',fontweight='bold')
ax[25].set_xlabel('t_sio2(aq) mol/L'  ,fontweight='bold')
ax[26].set_xlabel('t_so4-2 mg/L'  ,fontweight='bold')
ax[27].set_xlabel('t_so4-2 mg/L'  ,fontweight='bold')
ax[28].set_xlabel('t_hco3- mg/L'  ,fontweight='bold')

for a in ax:
    a.grid()
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

output_name = 'figure/'+'chemcal'+'.png'
fig.savefig(output_name, format='png', dpi=100)

#fig.close()
#for i in np.arange(plot_every):
#    opt.next()
#    gas.next()
#    sod.next()
#    aqu.next()
    


