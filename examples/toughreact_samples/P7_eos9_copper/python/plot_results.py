import os
# this script plots the output times. 
#for ii in opt.times[-1]:
if not os.path.exists('figure'):
        os.makedirs('figure')
reshape_format=[11,7]
y_mtx=Amic_aqu.element.DataFrame['Y'][1:].values.reshape(reshape_format)
x_mtx=Amic_aqu.element.DataFrame['X'][1:].values.reshape(reshape_format)
opt.first()
Amic_gas.first()
Amic_sod.first()
for ii in opt.times[4::5]:

    fig = plt.figure(figsize=(16,12))
   

    fig.suptitle('Time='  "%0.2f" % (ii/86400/365)   +' years', fontsize=16,fontweight="bold")
    ax = [[] for i in range(30)]
    ax[0  ] = plt.subplot2grid((5, 6), (0, 0), colspan=1)
    ax[1  ] = plt.subplot2grid((5, 6), (0, 1), colspan=1)
    ax[2  ] = plt.subplot2grid((5, 6), (0, 2), colspan=1)
    ax[3  ] = plt.subplot2grid((5, 6), (0, 3), colspan=1)
    ax[4  ] = plt.subplot2grid((5, 6), (0, 4), colspan=1)
    ax[5  ] = plt.subplot2grid((5, 6), (0, 5), colspan=1)
    ax[6  ] = plt.subplot2grid((5, 6), (1, 0), colspan=1)
    ax[7  ] = plt.subplot2grid((5, 6), (1, 1), colspan=1)
    ax[8  ] = plt.subplot2grid((5, 6), (1, 2), colspan=1)
    ax[9  ] = plt.subplot2grid((5, 6), (1, 3), colspan=1)
    ax[10 ] = plt.subplot2grid((5, 6), (1, 4), colspan=1)
    ax[11 ] = plt.subplot2grid((5, 6), (1, 5), colspan=1)
    ax[12 ] = plt.subplot2grid((5, 6), (2, 0), colspan=1)
    ax[13 ] = plt.subplot2grid((5, 6), (2, 1), colspan=1)
    ax[14 ] = plt.subplot2grid((5, 6), (2, 2), colspan=1)
    ax[15 ] = plt.subplot2grid((5, 6), (2, 3), colspan=1)
    ax[16 ] = plt.subplot2grid((5, 6), (2, 4), colspan=1)
    ax[17 ] = plt.subplot2grid((5, 6), (2, 5), colspan=1)
    ax[18 ] = plt.subplot2grid((5, 6), (3, 0), colspan=1)
    ax[19 ] = plt.subplot2grid((5, 6), (3, 1), colspan=1)
    ax[20 ] = plt.subplot2grid((5, 6), (3, 2), colspan=1)
    ax[21 ] = plt.subplot2grid((5, 6), (3, 3), colspan=1)
    ax[22 ] = plt.subplot2grid((5, 6), (3, 4), colspan=1)
    ax[23 ] = plt.subplot2grid((5, 6), (3, 5), colspan=1)
    ax[24 ] = plt.subplot2grid((5, 6), (4, 0), colspan=1)
    ax[25 ] = plt.subplot2grid((5, 6), (4, 1), colspan=1)
    ax[26 ] = plt.subplot2grid((5, 6), (4, 2), colspan=1)
    ax[27 ] = plt.subplot2grid((5, 6), (4, 3), colspan=1)
    ax[28 ] = plt.subplot2grid((5, 6), (4, 4), colspan=1)
    ax[29 ] = plt.subplot2grid((5, 6), (4, 5), colspan=1)

    fig.subplots_adjust(hspace=.50,wspace=.5)
    fig.subplots_adjust(left=0.05, right=0.95, top=0.92, bottom=0.05)

    ax[0].scatter(Amic_aqu.element.DataFrame['X'],Amic_aqu.element.DataFrame['Y'])


    # opt.element.column_name
    sat_liquid_mtx = opt.element.DataFrame['S(liq)'  ] [1: ] .values.reshape(reshape_format)
    diffus_mtx     = opt.element.DataFrame['DIFFUS.' ] [1: ] .values.reshape(reshape_format)
    pcap_mtx       = opt.element.DataFrame['PCAP'    ] [1: ] .values.reshape(reshape_format)
    flow_first_column_ay=opt.connection.DataFrame.loc[mask_first_column_index_ay]


    # Amic_gas.element.column_name
    #t_mtx          = Amic_gas.element.DataFrame['T(C)'][1:].values.reshape(reshape_format) # temperature is found to be homogeneous in this case
    #rh_mtx          = Amic_gas.element.DataFrame['RH'][1:].values.reshape(reshape_format) # relative humidity is found to be homogeneous in this case
    sg_mtx          = Amic_gas.element.DataFrame['Sg'][1:].values.reshape(reshape_format) 
    o2_mtx          = Amic_gas.element.DataFrame['o2(g)'][1:].values.reshape(reshape_format) 

    #Amic_sod.element.column_name
    t_mtx             = Amic_sod.element.DataFrame['T(C)'        ] [1: ] .values.reshape(reshape_format)  # same value
    por_mtx           = Amic_sod.element.DataFrame['Porosity'    ] [1: ] .values.reshape(reshape_format)  # same value
    poros_chg_mtx     = Amic_sod.element.DataFrame['Poros_Chg'   ] [1: ] .values.reshape(reshape_format)  # same value not clear what does this term means
    permx_m2_mtx      = Amic_sod.element.DataFrame['Permx(m^2)'  ] [1: ] .values.reshape(reshape_format)  # same value
    KxPKx0_mtx        = Amic_sod.element.DataFrame['Kx/Kx0'      ] [1: ] .values.reshape(reshape_format)  # same value
    Permz_m2_mtx      = Amic_sod.element.DataFrame['Permz(m^2)'  ] [1: ] .values.reshape(reshape_format)  # same value
    KzPKz0_mtx        = Amic_sod.element.DataFrame['Kz/Kz0'      ] [1: ] .values.reshape(reshape_format)  # same value
    pyrite_mtx        = Amic_sod.element.DataFrame['pyrite'      ] [1: ] .values.reshape(reshape_format)  # same value
    chalcopyrit_mtx   = Amic_sod.element.DataFrame['chalcopyrit' ] [1: ] .values.reshape(reshape_format)  # same value
    magnetite_mtx     = Amic_sod.element.DataFrame['magnetite'   ] [1: ] .values.reshape(reshape_format)  # same value
    k_feldspar_mtx    = Amic_sod.element.DataFrame['k-feldspar'  ] [1: ] .values.reshape(reshape_format)  # same value
    albite_mtx        = Amic_sod.element.DataFrame['albite'      ] [1: ] .values.reshape(reshape_format)  # same value
    anorthite_mtx     = Amic_sod.element.DataFrame['anorthite'   ] [1: ] .values.reshape(reshape_format)  # same value
    annite_mtx        = Amic_sod.element.DataFrame['annite'      ] [1: ] .values.reshape(reshape_format)  # same value
    muscovite_mtx     = Amic_sod.element.DataFrame['muscovite'   ] [1: ] .values.reshape(reshape_format)  # same value
    anhydrite_mtx     = Amic_sod.element.DataFrame['anhydrite'   ] [1: ] .values.reshape(reshape_format)  # same value
    goethite_mtx      = Amic_sod.element.DataFrame['goethite'    ] [1: ] .values.reshape(reshape_format)  # same value
    chalcocite_mtx    = Amic_sod.element.DataFrame['chalcocite'  ] [1: ] .values.reshape(reshape_format)  # same value
    covellite_mtx     = Amic_sod.element.DataFrame['covellite'   ] [1: ] .values.reshape(reshape_format)  # same value
    kaolinite_mtx     = Amic_sod.element.DataFrame['kaolinite'   ] [1: ] .values.reshape(reshape_format)  # same value
    sio2_am_mtx       = Amic_sod.element.DataFrame['sio2(am)'    ] [1: ] .values.reshape(reshape_format)  # same value
    alunite_mtx       = Amic_sod.element.DataFrame['alunite'     ] [1: ] .values.reshape(reshape_format)  # same value
    

    im1 = ax[1 ].contourf(x_mtx , y_mtx , sat_liquid_mtx )
    im2 = ax[2 ].contourf(x_mtx , y_mtx , diffus_mtx     )
    im3 = ax[3 ].contourf(x_mtx , y_mtx , pcap_mtx       )
    im4 = ax[4 ].contourf(x_mtx , y_mtx , sg_mtx         )
    im5 = ax[5 ].contourf(x_mtx , y_mtx , o2_mtx         )
    im6 = ax[6 ].contourf(x_mtx , y_mtx , por_mtx        )
    im7 = ax[7 ].contourf(x_mtx , y_mtx , poros_chg_mtx  )
    im8 = ax[8 ].contourf(x_mtx , y_mtx , permx_m2_mtx   )
    im9 = ax[9 ].contourf(x_mtx , y_mtx , KxPKx0_mtx     )
    im10= ax[10].contourf(x_mtx , y_mtx , Permz_m2_mtx   )
    im11= ax[11].contourf(x_mtx , y_mtx , KzPKz0_mtx     )
    im12= ax[12].contourf(x_mtx , y_mtx , pyrite_mtx     )
    im13= ax[13].contourf(x_mtx , y_mtx , chalcopyrit_mtx)
    im14= ax[14].contourf(x_mtx , y_mtx , magnetite_mtx  )
    im15= ax[15].contourf(x_mtx , y_mtx , k_feldspar_mtx )
    im16= ax[16].contourf(x_mtx , y_mtx , albite_mtx     )
    im17= ax[17].contourf(x_mtx , y_mtx , anorthite_mtx  )
    im18= ax[18].contourf(x_mtx , y_mtx , annite_mtx     )
    im19= ax[19].contourf(x_mtx , y_mtx , muscovite_mtx  )
    im20= ax[20].contourf(x_mtx , y_mtx , anhydrite_mtx  )
    im21= ax[21].contourf(x_mtx , y_mtx , goethite_mtx   )
    im22= ax[22].contourf(x_mtx , y_mtx , chalcocite_mtx )
    im23= ax[23].contourf(x_mtx , y_mtx , covellite_mtx  )
    im24= ax[24].contourf(x_mtx , y_mtx , kaolinite_mtx  )
    im25= ax[25].contourf(x_mtx , y_mtx , sio2_am_mtx    )
    im26= ax[26].contourf(x_mtx , y_mtx , alunite_mtx    )
    im27= ax[27].plot(flow_first_column_ay['FLO(LIQ.)'],y_mtx[1:,0]  )
    im28= ax[28].plot(flow_first_column_ay['VEL(LIQ.)'],y_mtx[1:,0] )
    im29= ax[29].plot(sat_liquid_mtx[:,0], y_mtx[:,0]  )

    #  a confirmation flow_first_column_ay['FLO(LIQ.)']/sat_liquid_mtx[:-1,0]/flow_first_column_ay['VEL(LIQ.)'] 
    # essentially 
    # FLO(LIQ.) [kg/s] = por * sat * VEL(LIQ.) [m3/s]  * density   [kg/m3]  
    # the unit of FLO(LIQ.) can be confirmated by the lower value as -5e-7 [kg/s], same as the input in GENER.
        


    fig.colorbar(im1 , ax=ax[1 ])
    fig.colorbar(im2 , ax=ax[2 ])
    fig.colorbar(im3 , ax=ax[3 ])
    fig.colorbar(im4 , ax=ax[4 ])
    fig.colorbar(im5 , ax=ax[5 ])
    fig.colorbar(im6 , ax=ax[6 ])
    fig.colorbar(im7 , ax=ax[7 ])
    fig.colorbar(im8 , ax=ax[8 ])
    fig.colorbar(im9 , ax=ax[9 ])
    fig.colorbar(im10, ax=ax[10])
    fig.colorbar(im11, ax=ax[11])
    fig.colorbar(im12, ax=ax[12])
    fig.colorbar(im13, ax=ax[13])
    fig.colorbar(im14, ax=ax[14])
    fig.colorbar(im15, ax=ax[15])
    fig.colorbar(im16, ax=ax[16])
    fig.colorbar(im17, ax=ax[17])
    fig.colorbar(im18, ax=ax[18])
    fig.colorbar(im19, ax=ax[19])
    fig.colorbar(im20, ax=ax[20])
    fig.colorbar(im21, ax=ax[21])
    fig.colorbar(im22, ax=ax[22])
    fig.colorbar(im23, ax=ax[23])
    fig.colorbar(im24, ax=ax[24])
    fig.colorbar(im25, ax=ax[25])
    fig.colorbar(im26, ax=ax[26])
    #fig.colorbar(im27, ax=ax[27])
    #fig.colorbar(im28, ax=ax[28])
    #fig.colorbar(im29, ax=ax[29])


    #ax[1].set_title('Saturation',x=0.04,y=0.8,fontweight='bold')
    ax[1 ].set_title('Liquid Saturation' , fontweight='bold')
    ax[2 ].set_title('Diffus'            , fontweight='bold')
    ax[3 ].set_title('Cap. Pre.'         , fontweight='bold')
    ax[4 ].set_title('Gas Saturation'    , fontweight='bold')
    ax[5 ].set_title('Oxygen'            , fontweight='bold')
    ax[6 ].set_title('Porosity'          , fontweight='bold')
    ax[7 ].set_title('Porosity change'   , fontweight='bold')
    ax[8 ].set_title('Permeability (m2)' , fontweight='bold')
    ax[9 ].set_title('Kx/Kx0'      , fontweight='bold')
    ax[10].set_title('Permz(m^2)'  , fontweight='bold')
    ax[11].set_title('Kz/Kz0'      , fontweight='bold')
    ax[12].set_title('pyrite'      , fontweight='bold')
    ax[13].set_title('chalcopyrit' , fontweight='bold')
    ax[14].set_title('magnetite'   , fontweight='bold')
    ax[15].set_title('k-feldspar'  , fontweight='bold')
    ax[16].set_title('albite'      , fontweight='bold')
    ax[17].set_title('anorthite'   , fontweight='bold')
    ax[18].set_title('annite'      , fontweight='bold')
    ax[19].set_title('muscovite'   , fontweight='bold')
    ax[20].set_title('anhydrite'   , fontweight='bold')
    ax[21].set_title('goethite'    , fontweight='bold')
    ax[22].set_title('chalcocite'  , fontweight='bold')
    ax[23].set_title('covellite'   , fontweight='bold')
    ax[24].set_title('kaolinite'   , fontweight='bold')
    ax[25].set_title('sio2(am)'    , fontweight='bold')
    ax[26].set_title('alunite'     , fontweight='bold')
    ax[27].set_title('FLO(LIQ.)_fra'     , fontweight='bold')
    ax[28].set_title('VEL(LIQ.)_fra'     , fontweight='bold')
    ax[29].set_title('sat_liq_fra'     , fontweight='bold')


    plt.show(block=False)
    output_name = 'figure/'+str(ii)+'.jpg'
    fig.savefig(output_name, format='jpg', dpi=100)
    opt.next()
    opt.next()
    opt.next()
    opt.next()

    Amic_gas.next()
    Amic_gas.next()
    Amic_gas.next()
    Amic_gas.next()

    Amic_sod.next()
    Amic_sod.next()
    Amic_sod.next()
    Amic_sod.next()


['2  10', '3  10']


inp.grid.connection['2  10', '3  10']   #how to return index?


# [('    1', '2   1'),
#  ('2   1', '3   1'), 
#  ('3   1', '4   1'),
#  ('4   1', '5   1'),
#  ('5   1', '6   1'),
#  ('6   1', '7   1'),
#  ('7   1', '8   1'),  
#  ('7   1', '8   1'),
#  ('7   1', '8   1'), 
#  ('7   1', '8   1'),
#  ]

#1
#2
#3
#4
#5
#6
#7
#8
#9
#10
#11
#12
#13
#14
#15
#16
#17
#18
#19
#20
#21
#22
#23
#24
#25
#26
#27
#28
#29
#30

