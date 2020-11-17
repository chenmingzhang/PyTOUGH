#np.concatinate([aqu.times,aqu.times])


bb=np.vstack(np.transpose([aqu.times,aqu.tx_mtx['pH'][:,-2],aqu.tx_mtx['pH'][:,-3],aqu.tx_mtx['pH'][:,-4,], 
    aqu.tx_mtx['t_so4-2'][:,-2] * mmass_sulphate_kgPmol* mgPkg,
    aqu.tx_mtx['t_so4-2'][:,-3] * mmass_sulphate_kgPmol* mgPkg, 
    aqu.tx_mtx['t_so4-2'][:,-4] * mmass_sulphate_kgPmol* mgPkg,   
    aqu.tx_mtx['t_fe+2'][:,-2] * mmass_iron2_kgPmol* mgPkg,
    aqu.tx_mtx['t_fe+2'][:,-3] * mmass_iron2_kgPmol* mgPkg,
    aqu.tx_mtx['t_fe+2'][:,-4] * mmass_iron2_kgPmol* mgPkg,
    aqu.tx_mtx['t_ca+2'][:,-2] * mmass_ca_kgPmol* mgPkg,
    aqu.tx_mtx['t_ca+2'][:,-3] * mmass_ca_kgPmol* mgPkg,
    aqu.tx_mtx['t_ca+2'][:,-4] * mmass_ca_kgPmol* mgPkg,
    aqu.tx_mtx['t_mg+2'][:,-2] * mmass_mg_kgPmol* mgPkg,
    aqu.tx_mtx['t_mg+2'][:,-3] * mmass_mg_kgPmol* mgPkg,
    aqu.tx_mtx['t_mg+2'][:,-4] * mmass_mg_kgPmol* mgPkg
    ]))
with open('calculated_results.csv', 'wb') as f:
    f.write(b'TIME (years), \
        pH simulated Column 6,\
        pH simulated Column 6,\
        pH simulated Column 6,\
        so4-2 simulated Column 6,\
        so4-2 simulated Column 6,\
        so4-2 simulated Column 6,\
        fe+2 simulated Column 6,\
        fe+2 simulated Column 6,\
        fe+2 simulated Column 6,\
        ca+2 simulated Column 6,\
        ca+2 simulated Column 6,\
        ca+2 simulated Column 6,\
        mg+2 simulated Column 6,\
        mg+2 simulated Column 6,\
        mg+2 simulated Column 6,\
        \n')
    #f.write(bytes("SP,"+lists+"\n","UTF-8"))
    #Used this line for a variable list of numbers
    np.savetxt(f, bb, delimiter=",")

cc=np.vstack(np.transpose([
    field_data['pH']['years'],
    field_data['pH'][1],
    field_data['pH'][2],
    field_data['pH'][3],
    field_data['pH'][4],
    field_data['pH'][5],
    field_data['pH'][6],
    ]))
with open('monitored_pH.csv', 'wb') as f:
    f.write(b'TIME (years),pH monitored Column 1 ,pH monitored Column 2, pH monitored Column 3\n')
    np.savetxt(f, cc, delimiter=",")

cc=np.vstack(np.transpose([
    field_data['col1'].loc['years'],
    field_data['col1'].loc['Sulphate'],
    field_data['col2'].loc['Sulphate'],
    field_data['col3'].loc['Sulphate'],
    field_data['col4'].loc['Sulphate'],
    field_data['col5'].loc['Sulphate'],
    field_data['col6'].loc['Sulphate'],
    field_data['col1'].loc['Fe Total'] ,
    field_data['col2'].loc['Fe Total'] ,
    field_data['col3'].loc['Fe Total'] ,
    field_data['col4'].loc['Fe Total'] ,
    field_data['col5'].loc['Fe Total'] ,
    field_data['col6'].loc['Fe Total'] ,
    field_data['col1'].loc['Ca Total'] ,
    field_data['col2'].loc['Ca Total'] ,
    field_data['col3'].loc['Ca Total'] ,
    field_data['col4'].loc['Ca Total'] ,
    field_data['col5'].loc['Ca Total'] ,
    field_data['col6'].loc['Ca Total'] ,
    field_data['col1'].loc['Mg Total'] ,
    field_data['col2'].loc['Mg Total'] ,
    field_data['col3'].loc['Mg Total'] ,
    field_data['col4'].loc['Mg Total'] ,
    field_data['col5'].loc['Mg Total'] ,
    field_data['col6'].loc['Mg Total'] 
    ]))
with open('monitored_ion.csv', 'wb') as f:
    f.write(b'TIME (years),so4-2 monitored Column 1 ,so4-2 monitored Column 2, so4-2 monitored Column 3, so4-2 monitored Column 4, so4-2 monitored Column 5, so4-2 monitored Column 6, \
            fe+2 monitored Column 1 ,fe+2 monitored Column 2, fe+2 monitored Column 3, fe+2 monitored Column 4, fe+2 monitored Column 5, fe+2 monitored Column 6, \
            ca+2 monitored Column 1 ,ca+2 monitored Column 2, ca+2 monitored Column 3, ca+2 monitored Column 4, ca+2 monitored Column 5, ca+2 monitored Column 6, \
            mg+2 monitored Column 1 ,mg+2 monitored Column 2, mg+2 monitored Column 3, mg+2 monitored Column 4, mg+2 monitored Column 5, mg+2 monitored Column 6 \n')
    np.savetxt(f, cc, delimiter=",")

    

#np.savetxt("foo.csv", bb, delimiter=",")

