import pandas as pd
import matplotlib.pyplot as plt

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


