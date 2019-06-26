# this script plots the output times. 
#for ii in opt.times[-1]:
if not os.path.exists('figure'):
        os.makedirs('figure')
reshape_format=[11,7]
y_mtx=Amic_aqu.element.DataFrame['Y'][1:].values.reshape(reshape_format)
x_mtx=Amic_aqu.element.DataFrame['X'][1:].values.reshape(reshape_format)
opt.first()
for ii in opt.times:

    fig = plt.figure(figsize=(16,10))
    ax = [[] for i in range(7)]
    ax[0] = plt.subplot2grid((3, 4), (0, 0), colspan=1)
    ax[1] = plt.subplot2grid((3, 4), (0, 1), colspan=1)
    ax[2] = plt.subplot2grid((3, 4), (0, 2), colspan=1)
    ax[3] = plt.subplot2grid((3, 4), (0, 3), colspan=1)
    ax[4] = plt.subplot2grid((3, 4), (1, 0), colspan=1)
    ax[5] = plt.subplot2grid((3, 4), (1, 1), colspan=1)
    ax[6] = plt.subplot2grid((3, 4), (1, 2), colspan=1)

    fig.subplots_adjust(hspace=.20,wspace=.5)
    fig.subplots_adjust(left=0.1, right=0.89, top=0.97, bottom=0.05)



    ax[0].scatter(Amic_aqu.element.DataFrame['X'],Amic_aqu.element.DataFrame['Y'])


    # opt.element.column_name
    sat_liquid_mtx = opt.element.DataFrame['S(liq)'][1:].values.reshape(reshape_format)
    diffus_mtx     = opt.element.DataFrame['DIFFUS.'][1:].values.reshape(reshape_format)
    pcap_mtx       = opt.element.DataFrame['PCAP'][1:].values.reshape(reshape_format)


    # Amic_gas.element.column_name
    #t_mtx          = Amic_gas.element.DataFrame['T(C)'][1:].values.reshape(reshape_format) # temperature is found to be homogeneous in this case
    sg_mtx          = Amic_gas.element.DataFrame['Sg'][1:].values.reshape(reshape_format) 
    #rh_mtx          = Amic_gas.element.DataFrame['RH'][1:].values.reshape(reshape_format) # relative humidity is found to be homogeneous in this case
    o2_mtx          = Amic_gas.element.DataFrame['o2(g)'][1:].values.reshape(reshape_format) 

    #Amic_sod.element.column_name
    sg_mtx          = Amic_gas.element.DataFrame['Sg'][1:].values.reshape(reshape_format) 
    

    im1=ax[1].contourf(x_mtx,y_mtx,sat_liquid_mtx)
    im2=ax[2].contourf(x_mtx,y_mtx,diffus_mtx)
    im3=ax[3].contourf(x_mtx,y_mtx,pcap_mtx)
    im4=ax[4].contourf(x_mtx,y_mtx,sg_mtx)
    im5=ax[5].contourf(x_mtx,y_mtx,o2_mtx)

    fig.colorbar(im1,ax=ax[1])
    fig.colorbar(im2,ax=ax[2])
    fig.colorbar(im3,ax=ax[3])
    fig.colorbar(im4,ax=ax[4])
    fig.colorbar(im4,ax=ax[5])


    #ax[1].set_title('Saturation',x=0.04,y=0.8,fontweight='bold')
    ax[1].set_title('Liquid Saturation',fontweight='bold')
    ax[2].set_title('Diffus',fontweight='bold')
    ax[3].set_title('Cap. Pre.',fontweight='bold')
    ax[4].set_title('Gas Saturation',fontweight='bold')
    ax[5].set_title('oxygen',fontweight='bold')


    plt.show(block=False)
    output_name = 'figure/'+str(ii)+'.jpg'
    fig.savefig(output_name, format='jpg', dpi=100)
    opt.next()


