# this script plots the output times. 
#for ii in opt.times[-1]:
if not os.path.exists('figure'):
        os.makedirs('figure')
y_mtx=Amic_aqu.element.DataFrame['Y'][1:].values.reshape(11,7)
x_mtx=Amic_aqu.element.DataFrame['X'][1:].values.reshape(11,7)
opt.first()
for ii in opt.times:

    fig = plt.figure(figsize=(16,10))
    ax = [[] for i in range(7)]
    ax[0] = plt.subplot2grid((3, 4), (0, 0), colspan=1)
    ax[1] = plt.subplot2grid((3, 4), (0, 1), colspan=1)
    ax[2] = plt.subplot2grid((3, 4), (0, 2), colspan=1)
    ax[3] = plt.subplot2grid((3, 4), (0, 3), colspan=1)
    ax[4] = plt.subplot2grid(4, 2), (4, 0), colspan=1)
    ax[5] = plt.subplot2grid((4, 2), (5, 0), colspan=1)
    ax[6] = plt.subplot2grid((4, 2), (6, 0), colspan=1)

    fig.subplots_adjust(hspace=.20)
    fig.subplots_adjust(left=0.1, right=0.89, top=0.97, bottom=0.05)



    ax[0].scatter(Amic_aqu.element.DataFrame['X'],Amic_aqu.element.DataFrame['Y'])



    sat_liquid_mtx=opt.element.DataFrame['S(liq)'][1:].values.reshape(11,7)
    diffus_mtx=opt.element.DataFrame['DIFFUS.'][1:].values.reshape(11,7)
    pcap_mtx=opt.element.DataFrame['PCAP'][1:].values.reshape(11,7)

    ax[1].contourf(x_mtx,y_mtx,sat_liquid_mtx)
    #ax[1]=plt.coutour(Amic_aqu.element.DataFrame['X'],Amic_aqu.element.DataFrame['Y'],Amic_aqu.element.DataFrame['S(liq)'])
    ax[2].contourf(x_mtx,y_mtx,diffus_mtx)
    ax[3].contourf(x_mtx,y_mtx,pcap_mtx)
    plt.show(block=False)
    output_name = 'figure/'+str(ii)+'.jpg'
    fig.savefig(output_name, format='jpg', dpi=100)
    opt.next()


