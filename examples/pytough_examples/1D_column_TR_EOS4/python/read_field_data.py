import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # disabled all the jumping out figures

field_data={}
field_data['pH']= pd.read_excel (r'../Document/200623_Water_Results_Column_Leach_Experiment.xlsx', sheet_name='ph',parse_dates=True,index_col=0)
field_data['pH']['days']= (field_data['pH'].index-field_data['pH'].index[0]).days
field_data['pH']['years']= field_data['pH']['days']/365.25


## result plotting
#fig = plt.figure(figsize=(16,12))
#
#plt.plot(field_data['pH']['days'],field_data['pH'][1],':o',label='Measurement 1')
#plt.plot(field_data['pH']['days'],field_data['pH'][2],':o',label='Measurement 2')
#plt.plot(field_data['pH']['days'],field_data['pH'][3],':o',label='Measurement 3')
#plt.plot(field_data['pH']['days'],field_data['pH'][3],':o',label='Measurement 4')
#plt.plot(field_data['pH']['days'],field_data['pH'][4],':o',label='Measurement 5')
#plt.plot(field_data['pH']['days'],field_data['pH'][5],':o',label='Measurement 6')
#
#plt.legend(bbox_to_anchor=(1.02, 0.9), loc=2, borderaxespad=0.)
#plt.show()


field_data['col1']= pd.read_excel (r'../Document/Master_SR_Column_Leach_Experiment.xlsx',sheet_name='Col 1',header=3,index_col=0,usecols="C,E:J",skiprows=0)
field_data['col2']= pd.read_excel (r'../Document/Master_SR_Column_Leach_Experiment.xlsx',sheet_name='Col 2',header=3,index_col=0,usecols="C,E:J",skiprows=0)
field_data['col3']= pd.read_excel (r'../Document/Master_SR_Column_Leach_Experiment.xlsx',sheet_name='Col 3',header=3,index_col=0,usecols="C,E:J",skiprows=0)
field_data['col4']= pd.read_excel (r'../Document/Master_SR_Column_Leach_Experiment.xlsx',sheet_name='Col 4',header=3,index_col=0,usecols="C,E:J",skiprows=0)
field_data['col5']= pd.read_excel (r'../Document/Master_SR_Column_Leach_Experiment.xlsx',sheet_name='Col 5',header=3,index_col=0,usecols="C,E:J",skiprows=0)
field_data['col6']= pd.read_excel (r'../Document/Master_SR_Column_Leach_Experiment.xlsx',sheet_name='Col 6',header=3,index_col=0,usecols="C,E:J",skiprows=0)


start_date=pd.Timestamp('2017-12-01 00:00:00')
field_data['col1'].loc['days']= (field_data['col1'].columns-start_date).days
field_data['col2'].loc['days']= (field_data['col2'].columns-start_date).days
field_data['col3'].loc['days']= (field_data['col3'].columns-start_date).days
field_data['col4'].loc['days']= (field_data['col4'].columns-start_date).days
field_data['col5'].loc['days']= (field_data['col5'].columns-start_date).days
field_data['col6'].loc['days']= (field_data['col6'].columns-start_date).days




#plot ph value
fig = plt.figure(figsize=(16,12))

plt.plot(field_data['col1'].loc['days'],field_data['col1'].loc['Sulphate'] , ':o',label='Col 1')
plt.plot(field_data['col2'].loc['days'],field_data['col2'].loc['Sulphate'] , ':o',label='Col 2')
plt.plot(field_data['col3'].loc['days'],field_data['col3'].loc['Sulphate'] , ':o',label='Col 3')
plt.plot(field_data['col4'].loc['days'],field_data['col4'].loc['Sulphate'] , ':o',label='Col 4')
plt.plot(field_data['col5'].loc['days'],field_data['col5'].loc['Sulphate'] , ':o',label='Col 5')
plt.plot(field_data['col6'].loc['days'],field_data['col6'].loc['Sulphate'] , ':o',label='Col 6')

plt.legend(bbox_to_anchor=(1.02, 0.9), loc=2, borderaxespad=0.)

output_name = 'figure/'+'Sulphate'+'.png'
fig.savefig(output_name, format='png', dpi=100)
