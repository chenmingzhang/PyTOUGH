import os # this script plots the output times.  #for ii in opt.times[-1]: plt.rcParams["axes.labelweight"] = "bold"
import pandas as pd
if not os.path.exists('figure'):
        os.makedirs('figure')
y_mtx=aqu.element.DataFrame['Y'][1:].values.reshape(reshape_format)
x_mtx=aqu.element.DataFrame['X'][1:].values.reshape(reshape_format)


opt.first()
gas.first()
sod.first()
aqu.first()
# ignore the first initial value.
a=opt.next()
gas.next()
sod.next()
aqu.next()
opt_pd_max=opt.element.DataFrame.max()
gas_pd_max=gas.element.DataFrame.max()
sod_pd_max=sod.element.DataFrame.max()
aqu_pd_max=aqu.element.DataFrame.max()
opt_pd_min=opt.element.DataFrame.min()
gas_pd_min=gas.element.DataFrame.min()
sod_pd_min=sod.element.DataFrame.min()
aqu_pd_min=aqu.element.DataFrame.min()


while a==True:
    a=opt.element.DataFrame.max()
    opt_pd_max=pd.concat([opt_pd_max,a],axis=1)
    a=opt.element.DataFrame.min()
    opt_pd_min=pd.concat([opt_pd_min,a],axis=1)

    a=gas.element.DataFrame.max()
    gas_pd_max=pd.concat([gas_pd_max,a],axis=1)
    a=gas.element.DataFrame.min()
    gas_pd_min=pd.concat([gas_pd_min,a],axis=1)

    a=sod.element.DataFrame.max()
    sod_pd_max=pd.concat([sod_pd_max,a],axis=1)
    a=sod.element.DataFrame.min()
    sod_pd_min=pd.concat([sod_pd_min,a],axis=1)

    a=aqu.element.DataFrame.max()
    aqu_pd_max=pd.concat([aqu_pd_max,a],axis=1)
    a=aqu.element.DataFrame.min()
    aqu_pd_min=pd.concat([aqu_pd_min,a],axis=1)
    a=opt.next()
    gas.next()
    sod.next()
    aqu.next()
    

opt_max_ay=opt_pd_max.max(axis=1);opt_min_ay=opt_pd_min.min(axis=1)
gas_max_ay=gas_pd_max.max(axis=1);gas_min_ay=gas_pd_min.min(axis=1)
aqu_max_ay=aqu_pd_max.max(axis=1);aqu_min_ay=aqu_pd_min.min(axis=1)
sod_max_ay=sod_pd_max.max(axis=1);sod_min_ay=sod_pd_min.min(axis=1)




opt.first()
gas.first()
sod.first()
aqu.first()
plot_every=5
for ii in opt.times[4::plot_every]:

    fig = plt.figure(figsize=(20,16))
   

    tlt =('opt.time='  "%0.2f" % (opt.time/86400/365)   +' years' 
        + ', sod.time='  "%0.2f" % (sod.time   ) +' years'
        ', aqu.time='  "%0.2f" % (aqu.time   ) +' years'
        ', aqu.time='  "%0.2f" % (gas.time   ) +' years')
    fig.suptitle(   tlt     , fontsize=16,fontweight="bold")
    print(tlt)
    no_row=7
    no_col=7
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

    ax[0].scatter(aqu.element.DataFrame['X'],aqu.element.DataFrame['Y'])


    # opt.element.column_name
    # ['PRES', 'S(liq)', 'PCAP', 'K(rel)', 'DIFFUS.']
    # NOTE: capillary pressure is negative in TOUGH
    sat_liquid_mtx    = opt.element.DataFrame['S(liq)'  ].values.reshape(reshape_format)
    diffus_mtx        = opt.element.DataFrame['DIFFUS.' ].values.reshape(reshape_format)
    pcap_mtx          = opt.element.DataFrame['PCAP'    ].values.reshape(reshape_format)
    flow_first_column_ay=opt.connection.DataFrame.loc[mask_first_column_index_ay]


    #aqu.get_index() --> get the current index number
    # gas.element.column_name
    #t_mtx            = gas.element.DataFrame['T(C)'][1:].values.reshape(reshape_format) # temperature is found to be homogeneous in this case
    #rh_mtx           = gas.element.DataFrame['RH'][1:].values.reshape(reshape_format) # relative humidity is found to be homogeneous in this case
    sg_mtx            = gas.element.DataFrame['Sg'   ][1:].values.reshape(reshape_format) 
    o2_mtx            = gas.element.DataFrame['o2(g)'][1:].values.reshape(reshape_format) 

    #sod.element.column_name
    t_mtx             = sod.element.DataFrame['T(C)'        ] [1: ] .values.reshape(reshape_format)  # same value
    por_mtx           = sod.element.DataFrame['Porosity'    ] [1: ] .values.reshape(reshape_format)  # same value
    poros_chg_mtx     = sod.element.DataFrame['Poros_Chg'   ] [1: ] .values.reshape(reshape_format)  # same value not clear what does this term means
    permx_m2_mtx      = sod.element.DataFrame['Permx(m^2)'  ] [1: ] .values.reshape(reshape_format)  # same value
    KxPKx0_mtx        = sod.element.DataFrame['Kx/Kx0'      ] [1: ] .values.reshape(reshape_format)  # same value
    Permz_m2_mtx      = sod.element.DataFrame['Permz(m^2)'  ] [1: ] .values.reshape(reshape_format)  # same value
    KzPKz0_mtx        = sod.element.DataFrame['Kz/Kz0'      ] [1: ] .values.reshape(reshape_format)  # same value
    pyrite_mtx        = sod.element.DataFrame['pyrite'      ] [1: ] .values.reshape(reshape_format)  # same value
    chalcopyrit_mtx   = sod.element.DataFrame['chalcopyrit' ] [1: ] .values.reshape(reshape_format)  # same value
    magnetite_mtx     = sod.element.DataFrame['magnetite'   ] [1: ] .values.reshape(reshape_format)  # same value
    k_feldspar_mtx    = sod.element.DataFrame['k-feldspar'  ] [1: ] .values.reshape(reshape_format)  # same value
    albite_mtx        = sod.element.DataFrame['albite'      ] [1: ] .values.reshape(reshape_format)  # same value
    anorthite_mtx     = sod.element.DataFrame['anorthite'   ] [1: ] .values.reshape(reshape_format)  # same value
    annite_mtx        = sod.element.DataFrame['annite'      ] [1: ] .values.reshape(reshape_format)  # same value
    muscovite_mtx     = sod.element.DataFrame['muscovite'   ] [1: ] .values.reshape(reshape_format)  # same value
    anhydrite_mtx     = sod.element.DataFrame['anhydrite'   ] [1: ] .values.reshape(reshape_format)  # same value
    goethite_mtx      = sod.element.DataFrame['goethite'    ] [1: ] .values.reshape(reshape_format)  # same value
    chalcocite_mtx    = sod.element.DataFrame['chalcocite'  ] [1: ] .values.reshape(reshape_format)  # same value
    covellite_mtx     = sod.element.DataFrame['covellite'   ] [1: ] .values.reshape(reshape_format)  # same value
    kaolinite_mtx     = sod.element.DataFrame['kaolinite'   ] [1: ] .values.reshape(reshape_format)  # same value
    sio2_am_mtx       = sod.element.DataFrame['sio2(am)'    ] [1: ] .values.reshape(reshape_format)  # same value
    alunite_mtx       = sod.element.DataFrame['alunite'     ] [1: ] .values.reshape(reshape_format)  # same value
    
    
    
    #aqu.element.column_name
    #conclusion  aqu_sg_mtx + aqu_sl_mtx  ==1 
    # ['X', 'Y', 'Z', 'P(bar)', 'Sg', 'Sl', 'T(C)', 'aH2O', 'pH', 't_so4-2','t_fe+2', 't_cu+2', 
    #'t_na+', 't_k+', 't_ca+2', 't_alo2-', 't_sio2(aq)', 't_cl-']
    aqu_p_bar_mtx    = aqu.element.DataFrame['P(bar)'       ] [1: ] .values.reshape(reshape_format)
    aqu_sg_mtx       = aqu.element.DataFrame['Sg'           ] [1: ] .values.reshape(reshape_format)
    aqu_sl_mtx       = aqu.element.DataFrame['Sl'           ] [1: ] .values.reshape(reshape_format)
    aqu_t_c_mtx      = aqu.element.DataFrame['T(C)'         ] [1: ] .values.reshape(reshape_format)
    aqu_ah2o_mtx     = aqu.element.DataFrame['aH2O'         ] [1: ] .values.reshape(reshape_format)
    aqu_ph_mtx       = aqu.element.DataFrame['pH'           ] [1: ] .values.reshape(reshape_format)
    
    aqu_t_so4_n2_mtx  = aqu.element.DataFrame['t_so4-2'    ] [1: ] .values.reshape(reshape_format)
    aqu_t_fe_p2_mtx   = aqu.element.DataFrame['t_fe+2'     ] [1: ] .values.reshape(reshape_format)
    aqu_t_cu_p2_mtx   = aqu.element.DataFrame['t_cu+2'     ] [1: ] .values.reshape(reshape_format)
    aqu_t_na_p1_mtx   = aqu.element.DataFrame['t_na+'      ] [1: ] .values.reshape(reshape_format)
    aqu_t_k_p1_mtx    = aqu.element.DataFrame['t_k+'       ] [1: ] .values.reshape(reshape_format)
    aqu_t_ca_p2_mtx   = aqu.element.DataFrame['t_ca+2'     ] [1: ] .values.reshape(reshape_format)
    aqu_t_alo2_n1_mtx = aqu.element.DataFrame['t_alo2-'    ] [1: ] .values.reshape(reshape_format)
    aqu_t_sio2_aq_mtx = aqu.element.DataFrame['t_sio2(aq)' ] [1: ] .values.reshape(reshape_format)
    #aqu_t_fe_p2      = aqu.element.DataFrame['t_fe+2'     ] [1: ] .values.reshape(reshape_format)
    #aqu_t_cu_p2      = aqu.element.DataFrame['t_cu+2'     ] [1: ] .values.reshape(reshape_format)
    #aqu_t_na_p1      = aqu.element.DataFrame['t_na+'      ] [1: ] .values.reshape(reshape_format)
    #aqu_t_k_p1       = aqu.element.DataFrame['t_k+'       ] [1: ] .values.reshape(reshape_format)
    #aqu_t_ca_p2      = aqu.element.DataFrame['t_ca+2'     ] [1: ] .values.reshape(reshape_format)
    #aqu_t_alo2_n1    = aqu.element.DataFrame['t_alo2-'    ] [1: ] .values.reshape(reshape_format)
    #aqu_t_sio2_aq    = aqu.element.DataFrame['t_sio2(aq)' ] [1: ] .values.reshape(reshape_format)
    aqu_t_cl_n1      = aqu.element.DataFrame['t_cl-'      ] [1: ] .values.reshape(reshape_format)




    
    #im1 = ax[1 ].contourf(x_mtx , y_mtx , sat_liquid_mtx ,vmin=opt_min_ay[  'S(liq)'     ], vmax=opt_max_ay['S(liq)'        ])
    #im2 = ax[2 ].contourf(x_mtx , y_mtx , diffus_mtx     ,vmin=opt_min_ay[  'DIFFUS.'    ], vmax=opt_max_ay['DIFFUS.'       ])
    #im3 = ax[3 ].contourf(x_mtx , y_mtx , pcap_mtx       ,vmin=opt_min_ay[  'PCAP'       ], vmax=opt_max_ay['PCAP'          ])

    #im4 = ax[4 ].contourf(x_mtx , y_mtx , sg_mtx         ,vmin=gas_min_ay[  'Sg'       ], vmax=gas_max_ay[ 'Sg'         ])
    #im5 = ax[5 ].contourf(x_mtx , y_mtx , o2_mtx         ,vmin=gas_min_ay[  'o2(g)'    ], vmax=gas_max_ay[ 'o2(g)'      ])

    #im6 = ax[6 ].contourf(x_mtx , y_mtx , por_mtx        ,vmin=sod_min_ay[ 'Porosity'         ], vmax=sod_max_ay['Porosity'         ])
    #im7 = ax[7 ].contourf(x_mtx , y_mtx , poros_chg_mtx  ,vmin=sod_min_ay[ 'Poros_Chg'        ], vmax=sod_max_ay['Poros_Chg'        ])
    #im8 = ax[8 ].contourf(x_mtx , y_mtx , permx_m2_mtx   ,vmin=sod_min_ay[ 'Permx(m^2)'       ], vmax=sod_max_ay['Permx(m^2)'       ])
    #im9 = ax[9 ].contourf(x_mtx , y_mtx , KxPKx0_mtx     ,vmin=sod_min_ay[ 'Kx/Kx0'           ], vmax=sod_max_ay['Kx/Kx0'           ])
    #im10= ax[10].contourf(x_mtx , y_mtx , Permz_m2_mtx   ,vmin=sod_min_ay[ 'Permz(m^2)'       ], vmax=sod_max_ay['Permz(m^2)'       ])
    #im11= ax[11].contourf(x_mtx , y_mtx , KzPKz0_mtx     ,vmin=sod_min_ay[ 'Kz/Kz0'           ], vmax=sod_max_ay['Kz/Kz0'           ])
    #im12= ax[12].contourf(x_mtx , y_mtx , pyrite_mtx     ,vmin=sod_min_ay[ 'pyrite'           ], vmax=sod_max_ay['pyrite'           ])
    #im13= ax[13].contourf(x_mtx , y_mtx , chalcopyrit_mtx,vmin=sod_min_ay[ 'chalcopyrit'      ], vmax=sod_max_ay['chalcopyrit'      ])
    #im14= ax[14].contourf(x_mtx , y_mtx , magnetite_mtx  ,vmin=sod_min_ay[ 'magnetite'        ], vmax=sod_max_ay['magnetite'        ])
    #im15= ax[15].contourf(x_mtx , y_mtx , k_feldspar_mtx ,vmin=sod_min_ay[ 'k-feldspar'       ], vmax=sod_max_ay['k-feldspar'       ])
    #im16= ax[16].contourf(x_mtx , y_mtx , albite_mtx     ,vmin=sod_min_ay[ 'albite'           ], vmax=sod_max_ay['albite'           ])
    #im17= ax[17].contourf(x_mtx , y_mtx , anorthite_mtx  ,vmin=sod_min_ay[ 'anorthite'        ], vmax=sod_max_ay['anorthite'        ])
    #im18= ax[18].contourf(x_mtx , y_mtx , annite_mtx     ,vmin=sod_min_ay[ 'annite'           ], vmax=sod_max_ay['annite'           ])
    #im19= ax[19].contourf(x_mtx , y_mtx , muscovite_mtx  ,vmin=sod_min_ay[ 'muscovite'        ], vmax=sod_max_ay['muscovite'        ])
    #im20= ax[20].contourf(x_mtx , y_mtx , anhydrite_mtx  ,vmin=sod_min_ay[ 'anhydrite'        ], vmax=sod_max_ay['anhydrite'        ])
    #im21= ax[21].contourf(x_mtx , y_mtx , goethite_mtx   ,vmin=sod_min_ay[ 'goethite'         ], vmax=sod_max_ay['goethite'         ])
    #im22= ax[22].contourf(x_mtx , y_mtx , chalcocite_mtx ,vmin=sod_min_ay[ 'chalcocite'       ], vmax=sod_max_ay['chalcocite'       ])
    #im23= ax[23].contourf(x_mtx , y_mtx , covellite_mtx  ,vmin=sod_min_ay[ 'covellite'        ], vmax=sod_max_ay['covellite'        ])
    #im24= ax[24].contourf(x_mtx , y_mtx , kaolinite_mtx  ,vmin=sod_min_ay[ 'kaolinite'        ], vmax=sod_max_ay['kaolinite'        ])
    #im25= ax[25].contourf(x_mtx , y_mtx , sio2_am_mtx    ,vmin=sod_min_ay[ 'sio2(am)'         ], vmax=sod_max_ay['sio2(am)'         ])
    #im26= ax[26].contourf(x_mtx , y_mtx , alunite_mtx    ,vmin=sod_min_ay[ 'alunite'          ], vmax=sod_max_ay['alunite'          ])
    #im27= ax[27].plot(flow_first_column_ay['FLO(LIQ.)'],y_mtx[1:,0]  )
    #im28= ax[28].plot(flow_first_column_ay['VEL(LIQ.)'],y_mtx[1:,0] )
    #im29= ax[29].plot(sat_liquid_mtx[:,0], y_mtx[:,0]  )
    #im30= ax[30].contourf(x_mtx , y_mtx , aqu_t_so4_n2_mtx   ,vmin=aqu_min_ay['t_so4-2'      ], vmax=aqu_max_ay['t_so4-2'       ]) 
    #im31= ax[31].contourf(x_mtx , y_mtx , aqu_t_fe_p2_mtx    ,vmin=aqu_min_ay['t_fe+2'       ], vmax=aqu_max_ay['t_fe+2'        ])
    #im32= ax[32].contourf(x_mtx , y_mtx , aqu_t_cu_p2_mtx    ,vmin=aqu_min_ay['t_cu+2'       ], vmax=aqu_max_ay['t_cu+2'        ])
    #im33= ax[33].contourf(x_mtx , y_mtx , aqu_t_na_p1_mtx    ,vmin=aqu_min_ay['t_na+'        ], vmax=aqu_max_ay['t_na+'         ])
    #im34= ax[34].contourf(x_mtx , y_mtx , aqu_t_k_p1_mtx     ,vmin=aqu_min_ay['t_k+'         ], vmax=aqu_max_ay['t_k+'          ])
    #im35= ax[35].contourf(x_mtx , y_mtx , aqu_t_ca_p2_mtx    ,vmin=aqu_min_ay['t_ca+2'       ], vmax=aqu_max_ay['t_ca+2'        ])
    #im36= ax[36].contourf(x_mtx , y_mtx , aqu_t_alo2_n1_mtx  ,vmin=aqu_min_ay['t_alo2-'      ], vmax=aqu_max_ay['t_alo2-'       ])
    #im37= ax[37].contourf(x_mtx , y_mtx , aqu_t_sio2_aq_mtx  ,vmin=aqu_min_ay['t_sio2(aq)'   ], vmax=aqu_max_ay['t_sio2(aq)'    ])
    #im38= ax[38].contourf(x_mtx , y_mtx , aqu_p_bar_mtx      ,vmin=aqu_min_ay['P(bar)'       ], vmax=aqu_max_ay['P(bar)'        ])
    #im39= ax[39].contourf(x_mtx , y_mtx , aqu_sg_mtx         ,vmin=aqu_min_ay['Sg'           ], vmax=aqu_max_ay['Sg'            ])
    #im40= ax[40].contourf(x_mtx , y_mtx , aqu_sl_mtx         ,vmin=aqu_min_ay['Sl'           ], vmax=aqu_max_ay['Sl'            ])
    #im41= ax[41].contourf(x_mtx , y_mtx , aqu_t_c_mtx        ,vmin=aqu_min_ay['T(C)'         ], vmax=aqu_max_ay['T(C)'          ])
    #im42= ax[42].contourf(x_mtx , y_mtx , aqu_ah2o_mtx       ,vmin=aqu_min_ay['aH2O'         ], vmax=aqu_max_ay['aH2O'          ])
    #im43= ax[43].contourf(x_mtx , y_mtx , aqu_ph_mtx         ,vmin=aqu_min_ay['pH'           ], vmax=aqu_max_ay['pH'            ])
    ##im44= ax[44].contourf(x_mtx , y_mtx , aqu_t_sio2_aq      ,vmin=aqu_min_ay['t_sio2(aq)'   ], vmax=aqu_max_ay['t_sio2(aq)'    ])
    #im45= ax[45].contourf(x_mtx , y_mtx , aqu_t_cl_n1        ,vmin=aqu_min_ay['t_cl-'        ], vmax=aqu_max_ay['t_cl-'         ])

    freq=10






    m1 =np.linspace(opt_min_ay[  'S(liq)'     ], opt_max_ay['S(liq)'      ],freq)
    m2 =np.linspace(opt_min_ay[  'DIFFUS.'    ], opt_max_ay['DIFFUS.'     ],freq)
    m3 =np.linspace(opt_min_ay[  'PCAP'       ], opt_max_ay['PCAP'        ],freq)
    m4 =np.linspace(gas_min_ay[  'Sg'         ], gas_max_ay[ 'Sg'         ],freq)
    m5 =np.linspace(gas_min_ay[  'o2(g)'      ], gas_max_ay[ 'o2(g)'      ],freq)
    m6 =np.linspace(sod_min_ay[ 'Porosity'    ], sod_max_ay['Porosity'    ],freq)
    m7 =np.linspace(sod_min_ay[ 'Poros_Chg'   ], sod_max_ay['Poros_Chg'   ],freq)
    m8 =np.linspace(sod_min_ay[ 'Permx(m^2)'  ], sod_max_ay['Permx(m^2)'  ],freq)
    m9 =np.linspace(sod_min_ay[ 'Kx/Kx0'      ], sod_max_ay['Kx/Kx0'      ],freq)
    m10=np.linspace(sod_min_ay[ 'Permz(m^2)'  ], sod_max_ay['Permz(m^2)'  ],freq)
    m11=np.linspace(sod_min_ay[ 'Kz/Kz0'      ], sod_max_ay['Kz/Kz0'      ],freq)
    m12=np.linspace(sod_min_ay[ 'pyrite'      ], sod_max_ay['pyrite'      ],freq)
    m13=np.linspace(sod_min_ay[ 'chalcopyrit' ], sod_max_ay['chalcopyrit' ],freq)
    m14=np.linspace(sod_min_ay[ 'magnetite'   ], sod_max_ay['magnetite'   ],freq)
    m15=np.linspace(sod_min_ay[ 'k-feldspar'  ], sod_max_ay['k-feldspar'  ],freq)
    m16=np.linspace(sod_min_ay[ 'albite'      ], sod_max_ay['albite'      ],freq)
    m17=np.linspace(sod_min_ay[ 'anorthite'   ], sod_max_ay['anorthite'   ],freq)
    m18=np.linspace(sod_min_ay[ 'annite'      ], sod_max_ay['annite'      ],freq)
    m19=np.linspace(sod_min_ay[ 'muscovite'   ], sod_max_ay['muscovite'   ],freq)
    m20=np.linspace(sod_min_ay[ 'anhydrite'   ], sod_max_ay['anhydrite'   ],freq)
    m21=np.linspace(sod_min_ay[ 'goethite'    ], sod_max_ay['goethite'    ],freq)
    m22=np.linspace(sod_min_ay[ 'chalcocite'  ], sod_max_ay['chalcocite'  ],freq)
    m23=np.linspace(sod_min_ay[ 'covellite'   ], sod_max_ay['covellite'   ],freq)
    m24=np.linspace(sod_min_ay[ 'kaolinite'   ], sod_max_ay['kaolinite'   ],freq)
    m25=np.linspace(sod_min_ay[ 'sio2(am)'    ], sod_max_ay['sio2(am)'    ],freq)
    m26=np.linspace(sod_min_ay[ 'alunite'     ], sod_max_ay['alunite'     ],freq)
    m30=np.linspace(aqu_min_ay['t_so4-2'      ], aqu_max_ay['t_so4-2'     ],freq)
    m31=np.linspace(aqu_min_ay['t_fe+2'       ], aqu_max_ay['t_fe+2'      ],freq)
    m32=np.linspace(aqu_min_ay['t_cu+2'       ], aqu_max_ay['t_cu+2'      ],freq)
    m33=np.linspace(aqu_min_ay['t_na+'        ], aqu_max_ay['t_na+'       ],freq)
    m34=np.linspace(aqu_min_ay['t_k+'         ], aqu_max_ay['t_k+'        ],freq)
    m35=np.linspace(aqu_min_ay['t_ca+2'       ], aqu_max_ay['t_ca+2'      ],freq)
    m36=np.linspace(aqu_min_ay['t_alo2-'      ], aqu_max_ay['t_alo2-'     ],freq)
    m37=np.linspace(aqu_min_ay['t_sio2(aq)'   ], aqu_max_ay['t_sio2(aq)'  ],freq)
    m38=np.linspace(aqu_min_ay['P(bar)'       ], aqu_max_ay['P(bar)'      ],freq)
    m39=np.linspace(aqu_min_ay['Sg'           ], aqu_max_ay['Sg'          ],freq)
    m40=np.linspace(aqu_min_ay['Sl'           ], aqu_max_ay['Sl'          ],freq)
    m41=np.linspace(aqu_min_ay['T(C)'         ], aqu_max_ay['T(C)'        ],freq)
    m42=np.linspace(aqu_min_ay['aH2O'         ], aqu_max_ay['aH2O'        ],freq)
    m43=np.linspace(aqu_min_ay['pH'           ], aqu_max_ay['pH'          ],freq)
    m45=np.linspace(aqu_min_ay['t_cl-'        ], aqu_max_ay['t_cl-'       ],freq)






    im1 = ax[1 ].contourf(x_mtx , y_mtx , sat_liquid_mtx     ,m1 )
    im2 = ax[2 ].contourf(x_mtx , y_mtx , diffus_mtx         ,m2 )
    im3 = ax[3 ].contourf(x_mtx , y_mtx , pcap_mtx           ,m3 )
    im4 = ax[4 ].contourf(x_mtx , y_mtx , sg_mtx             ,m4 )
    im5 = ax[5 ].contourf(x_mtx , y_mtx , o2_mtx             ,m5 )
    im6 = ax[6 ].contourf(x_mtx , y_mtx , por_mtx            ,m6 )
    im7 = ax[7 ].contourf(x_mtx , y_mtx , poros_chg_mtx      ,m7 )
    im8 = ax[8 ].contourf(x_mtx , y_mtx , permx_m2_mtx       ,m8 )
    im9 = ax[9 ].contourf(x_mtx , y_mtx , KxPKx0_mtx             )
    im10= ax[10].contourf(x_mtx , y_mtx , Permz_m2_mtx       ,m10)
    im11= ax[11].contourf(x_mtx , y_mtx , KzPKz0_mtx         )
    im12= ax[12].contourf(x_mtx , y_mtx , pyrite_mtx         ,m12)
    im13= ax[13].contourf(x_mtx , y_mtx , chalcopyrit_mtx    ,m13)
    im14= ax[14].contourf(x_mtx , y_mtx , magnetite_mtx      ,m14)
    im15= ax[15].contourf(x_mtx , y_mtx , k_feldspar_mtx     ,m15)
    im16= ax[16].contourf(x_mtx , y_mtx , albite_mtx         ,m16)
    im17= ax[17].contourf(x_mtx , y_mtx , anorthite_mtx      ,m17)
    im18= ax[18].contourf(x_mtx , y_mtx , annite_mtx         ,m18)
    im19= ax[19].contourf(x_mtx , y_mtx , muscovite_mtx      ,m19)
    im20= ax[20].contourf(x_mtx , y_mtx , anhydrite_mtx      ,m20)
    im21= ax[21].contourf(x_mtx , y_mtx , goethite_mtx       ,m21)
    im22= ax[22].contourf(x_mtx , y_mtx , chalcocite_mtx     ,m22)
    im23= ax[23].contourf(x_mtx , y_mtx , covellite_mtx      ,m23)
    im24= ax[24].contourf(x_mtx , y_mtx , kaolinite_mtx      ,m24)
    im25= ax[25].contourf(x_mtx , y_mtx , sio2_am_mtx        ,m25)
    im26= ax[26].contourf(x_mtx , y_mtx , alunite_mtx        ,m26)
    im30= ax[30].contourf(x_mtx , y_mtx , aqu_t_so4_n2_mtx   ,m30) 
    im31= ax[31].contourf(x_mtx , y_mtx , aqu_t_fe_p2_mtx    ,m31)
    im32= ax[32].contourf(x_mtx , y_mtx , aqu_t_cu_p2_mtx    ,m32)
    im33= ax[33].contourf(x_mtx , y_mtx , aqu_t_na_p1_mtx    ,m33)
    im34= ax[34].contourf(x_mtx , y_mtx , aqu_t_k_p1_mtx     ,m34)
    im35= ax[35].contourf(x_mtx , y_mtx , aqu_t_ca_p2_mtx    ,m35)
    im36= ax[36].contourf(x_mtx , y_mtx , aqu_t_alo2_n1_mtx  ,m36)
    im37= ax[37].contourf(x_mtx , y_mtx , aqu_t_sio2_aq_mtx  ,m37)
    im38= ax[38].contourf(x_mtx , y_mtx , aqu_p_bar_mtx      ,m38)
    im39= ax[39].contourf(x_mtx , y_mtx , aqu_sg_mtx         ,m39)
    im40= ax[40].contourf(x_mtx , y_mtx , aqu_sl_mtx         ,m40)
    im41= ax[41].contourf(x_mtx , y_mtx , aqu_t_c_mtx        )
    im42= ax[42].contourf(x_mtx , y_mtx , aqu_ah2o_mtx       ,m42)
    im43= ax[43].contourf(x_mtx , y_mtx , aqu_ph_mtx         ,m43)
    im45= ax[45].contourf(x_mtx , y_mtx , aqu_t_cl_n1        ,m45)

    im27= ax[27].plot(flow_first_column_ay['FLO(LIQ.)'],y_mtx[1:,0]  )
    im28= ax[28].plot(flow_first_column_ay['VEL(LIQ.)'],y_mtx[1:,0] )
    im29= ax[29].plot(sat_liquid_mtx[:,0], y_mtx[:,0]  )




    #  a confirmation flow_first_column_ay['FLO(LIQ.)']/sat_liquid_mtx[:-1,0]/flow_first_column_ay['VEL(LIQ.)'] 
    # essentially 
    # FLO(LIQ.) [kg/s] = por * sat * VEL(LIQ.) [m3/s]  * density   [kg/m3]  
    # the unit of FLO(LIQ.) can be confirmated by the lower value as -5e-7 [kg/s], same as the input in GENER.
        


    fig.colorbar(im1 , ax=ax[1 ], format='%.1e',ticks=m1 )
    fig.colorbar(im2 , ax=ax[2 ], format='%.1e',ticks=m2 )
    fig.colorbar(im3 , ax=ax[3 ], format='%.1e',ticks=m3 )
    fig.colorbar(im4 , ax=ax[4 ], format='%.1e',ticks=m4 )
    fig.colorbar(im5 , ax=ax[5 ], format='%.1e',ticks=m5 )
    fig.colorbar(im6 , ax=ax[6 ], format='%.1e',ticks=m6 )
    fig.colorbar(im7 , ax=ax[7 ], format='%.1e',ticks=m7 )
    fig.colorbar(im8 , ax=ax[8 ], format='%.1e',ticks=m8 )
    fig.colorbar(im9 , ax=ax[9 ], format='%.1e',ticks=m9 )
    fig.colorbar(im10, ax=ax[10], format='%.1e',ticks=m10)
    fig.colorbar(im11, ax=ax[11], format='%.1e',ticks=m11)
    fig.colorbar(im12, ax=ax[12], format='%.1e',ticks=m12)
    fig.colorbar(im13, ax=ax[13], format='%.1e',ticks=m13)
    fig.colorbar(im14, ax=ax[14], format='%.1e',ticks=m14)
    fig.colorbar(im15, ax=ax[15], format='%.1e',ticks=m15)
    fig.colorbar(im16, ax=ax[16], format='%.1e',ticks=m16)
    fig.colorbar(im17, ax=ax[17], format='%.1e',ticks=m17)
    fig.colorbar(im18, ax=ax[18], format='%.1e',ticks=m18)
    fig.colorbar(im19, ax=ax[19], format='%.1e',ticks=m19)
    fig.colorbar(im20, ax=ax[20], format='%.1e',ticks=m20)
    fig.colorbar(im21, ax=ax[21], format='%.1e',ticks=m21)
    fig.colorbar(im22, ax=ax[22], format='%.1e',ticks=m22)
    fig.colorbar(im23, ax=ax[23], format='%.1e',ticks=m23)
    fig.colorbar(im24, ax=ax[24], format='%.1e',ticks=m24)
    fig.colorbar(im25, ax=ax[25], format='%.1e',ticks=m25)
    fig.colorbar(im26, ax=ax[26], format='%.1e',ticks=m26)
    fig.colorbar(im30, ax=ax[30], format='%.1e',ticks=m30)
    fig.colorbar(im31, ax=ax[31], format='%.1e',ticks=m31)
    fig.colorbar(im32, ax=ax[32], format='%.1e',ticks=m32)
    fig.colorbar(im33, ax=ax[33], format='%.1e',ticks=m33)
    fig.colorbar(im34, ax=ax[34], format='%.1e',ticks=m34)
    fig.colorbar(im35, ax=ax[35], format='%.1e',ticks=m35)
    fig.colorbar(im36, ax=ax[36], format='%.1e',ticks=m36)
    fig.colorbar(im37, ax=ax[37], format='%.1e',ticks=m37)
    fig.colorbar(im38, ax=ax[38], format='%.1e',ticks=m38)
    fig.colorbar(im39, ax=ax[39], format='%.1e',ticks=m39)
    fig.colorbar(im40, ax=ax[40], format='%.1e',ticks=m40)
    fig.colorbar(im41, ax=ax[41], format='%.1e',ticks=m41)
    fig.colorbar(im42, ax=ax[42], format='%.1e',ticks=m42)
    fig.colorbar(im43, ax=ax[43], format='%.1e',ticks=m43)
    fig.colorbar(im45, ax=ax[45], format='%.1e',ticks=m45)

    #fig.colorbar(im44, ax=ax[44], format='%.1e')
    #fig.colorbar(im27, ax=ax[27])
    #fig.colorbar(im28, ax=ax[28])
    #fig.colorbar(im29, ax=ax[29])
    #ax[1].set_title('Saturation',x=0.04,y=0.8,fontweight='bold')
    ax[1 ].set_title('flow.out \n Liquid Saturation' , fontweight='bold')
    ax[2 ].set_title('flow.out \n Diffus'            , fontweight='bold')
    ax[3 ].set_title('flow.out \n Cap. Pre.'         , fontweight='bold')
    ax[4 ].set_title('gas \n Gas Saturation'    , fontweight='bold')
    ax[5 ].set_title('gas \n Oxygen'            , fontweight='bold')
    ax[6 ].set_title('sod \n Porosity'          , fontweight='bold')
    ax[7 ].set_title('sod \n Porosity change'   , fontweight='bold')
    ax[8 ].set_title('sod \n Permeability (m2)' , fontweight='bold')
    ax[9 ].set_title('sod \n Kx/Kx0'      , fontweight='bold')
    ax[10].set_title('sod \n Permz(m^2)'  , fontweight='bold')
    ax[11].set_title('sod \n Kz/Kz0'      , fontweight='bold')
    ax[12].set_title('sod \n pyrite'      , fontweight='bold')
    ax[13].set_title('sod \n chalcopyrit' , fontweight='bold')
    ax[14].set_title('sod \n magnetite'   , fontweight='bold')
    ax[15].set_title('sod \n k-feldspar'  , fontweight='bold')
    ax[16].set_title('sod \n albite'      , fontweight='bold')
    ax[17].set_title('sod \n anorthite'   , fontweight='bold')
    ax[18].set_title('sod \n annite'      , fontweight='bold')
    ax[19].set_title('sod \n muscovite'   , fontweight='bold')
    ax[20].set_title('sod \n anhydrite'   , fontweight='bold')
    ax[21].set_title('sod \n goethite'    , fontweight='bold')
    ax[22].set_title('sod \n chalcocite'  , fontweight='bold')
    ax[23].set_title('sod \n covellite'   , fontweight='bold')
    ax[24].set_title('sod \n kaolinite'   , fontweight='bold')
    ax[25].set_title('sod \n sio2(am)'    , fontweight='bold')
    ax[26].set_title('sod \n alunite'     , fontweight='bold')
    
    ax[27].set_title('flow.out \n FLO(LIQ.)_fra(kg/s)'     , fontweight='bold')
    ax[28].set_title('flow.out \n VEL(LIQ.)_fra(m3/s)'     , fontweight='bold')
    ax[29].set_title('flow.out \n sat_liq_fra'     , fontweight='bold')

    ax[30].set_title('aqu \n t_so4-2'    ,  fontweight='bold') 
    ax[31].set_title('aqu \n t_fe+2'     ,  fontweight='bold') 
    ax[32].set_title('aqu \n t_cu+2'     ,  fontweight='bold') 
    ax[33].set_title('aqu \n t_na+'      ,  fontweight='bold') 
    ax[34].set_title('aqu \n t_k+'       ,  fontweight='bold') 
    ax[35].set_title('aqu \n t_ca+2'     ,  fontweight='bold') 
    ax[36].set_title('aqu \n t_alo2-'    ,  fontweight='bold') 
    ax[37].set_title('aqu \n t_sio2(aq)' ,  fontweight='bold') 
    ax[38].set_title('aqu \n P(bar)'     ,  fontweight='bold') 
    ax[39].set_title('aqu \n Sg'         ,  fontweight='bold') 
    ax[40].set_title('aqu \n Sl'         ,  fontweight='bold') 
    ax[41].set_title('aqu \n T(C)'       ,  fontweight='bold') 
    ax[42].set_title('aqu \n aH2O'       ,  fontweight='bold') 
    ax[43].set_title('aqu \n pH'         ,  fontweight='bold') 
    #ax[44].set_title('aqu \n ',  fontweight='bold') 
    ax[45].set_title('aqu \n t_cl-'      ,  fontweight='bold') 

    plt.show(block=False)
    output_name = 'figure/'+str(ii)+'.jpg'
    fig.savefig(output_name, format='jpg', dpi=100)

    for i in np.arange(plot_every):
        opt.next()
        gas.next()
        sod.next()
        aqu.next()
    


