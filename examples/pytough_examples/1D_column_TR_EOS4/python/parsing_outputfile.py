from t2listing import *
import numpy as np
import matplotlib.pyplot as plt
import csv
import os
from t2data import *
from mpl_toolkits.mplot3d import Axes3D

print('Start parsing output file\n')

liquid_density_kgPm3   = 1000
water_molecular_weight = 0.018
kpaPpa                 = 1.e-3
R_value                = 8.3145
mPmm                   = 1.e-3
dayPs                  = 1./(3600*24)
T_kelven               = 273.15

title = 'flow.out'
# --- post-process the output ---------------------------
lst = t2listing(title)
dat = t2data('flow.inp')

connection_first_distance  = np.array([blk.distance[0] for blk in dat.grid.connectionlist])
connection_second_distance = np.array([blk.distance[1] for blk in dat.grid.connectionlist])
ele_depth_m                = np.cumsum(np.insert(connection_first_distance+connection_second_distance,0,0))
con_depth_m                = np.cumsum(connection_first_distance+np.insert(connection_second_distance[:-1], 0, 0))
                                        

element_coordinate_m=np.array([j.centre for j in inp.grid.blocklist])
ele_x_ay_all=np.array([i[0] for i in element_coordinate_m] )
ele_z_ay_all=np.array([i[2] for i in element_coordinate_m] )

#x_element_ay =[ i[2] for i in element_coordinate_m ]
#lst.element.column_name
#['P', 'T', 'SG', 'SL', 'XAIRG', 'XAIRL', 'PAIR', 'PCAP', 'DG', 'DL']
# XAIRG   ----   mass fraction of air in gas phase
# XAIRL   ----   mass fraction of air in liquid phase  ???? what does this mean?
# PAIR    ----   parial pressure of air ( i think it is air pressure)
# PCAP    ----   capillary pressure
# DL      ----   liquid density
# DG      ----   gas density

#lst.connection.column_name
#['FLOH', 'FLOH/FLOF', 'FLOF', 'FLO(GAS)', 'VAPDIF', 'FLO(LIQ.)', 'VEL(GAS)', 'VEL(LIQ.)']
#lst.generation.column_name
#['GENERATION RATE', 'ENTHALPY', 'FF(GAS)', 'FF(LIQ.)', 'P(WB)']


dg_xt_mtx_kgPm3          = np.array([lst.history(('e',i,'DG' ) )[1] for i in lst.element.row_name])   # two brackets is needed! gas density
dl_xt_mtx_kgPm3          = np.array([lst.history(('e',i,'DL'  ))[1] for i in lst.element.row_name])   # liquid density
sg_xt_mtx                = np.array([lst.history(('e',i,'SG'  ))[1] for i in lst.element.row_name])
sl_xt_mtx                = np.array([lst.history(('e',i,'SL'  ))[1] for i in lst.element.row_name])
p_xt_mtx_pa              = np.array([lst.history(('e',i,'P'   ))[1] for i in lst.element.row_name])   # gas pressure
pair_xt_mtx_pa           = np.array([lst.history(('e',i,'PAIR'))[1] for i in lst.element.row_name])   # air pressure
pcap_xt_mtx_pa           = np.array([lst.history(('e',i,'PCAP'))[1] for i in lst.element.row_name])
t_xt_mtx                 = np.array([lst.history(('e',i,'T'   ))[1] for i in lst.element.row_name])
xirg_xt_mtx              = 1-np.array([lst.history(('e',i,'XAIRG'))[1] for i in lst.element.row_name])     #vapor mass fraction in gas


dv_xt_mtx_kgPm3          =  dg_xt_mtx_kgPm3 * xirg_xt_mtx    # this is wrong
dv_sat_xt_mtx_kgPm3      =  1e-3*np.exp(19.819-4976/ ( t_xt_mtx +273.15   )   )
                                  

dl_con_loc_xt_mtx_kgPm3  = np.array( [ (i[:-1]+i[1:])/2 for i in dl_xt_mtx_kgPm3.T]).T
dg_con_loc_xt_mtx_kgPm3  = np.array( [ (i[:-1]+i[1:])/2 for i in dg_xt_mtx_kgPm3.T]).T
dv_con_loc_xt_mtx_kgPm3  = np.array( [ (i[:-1]+i[1:])/2 for i in dv_xt_mtx_kgPm3.T]).T  # this might be wrong
sl_con_loc_xt_mtx        = np.array( [ (i[:-1]+i[1:])/2 for i in sl_xt_mtx.T]).T 

dv_sat_con_loc_xt_mtx_kgPm3      =  np.array( [ (i[:-1]+i[1:])/2 for i in dv_sat_xt_mtx_kgPm3.T]).T
# we did not check the vapor density





#liquid_flow_xt_mtx_kgPs           = -np.array([lst.history(('c',i,'FLO(LIQ.)'))[1] for i in lst.connection.row_name])
flo_liq_xt_mtx_kgPs      = -np.array([lst.history(('c',i,'FLO(LIQ.)'))[1] for i in lst.connection.row_name])


flo_liq_xt_mtx_mmPday    = flo_liq_xt_mtx_kgPs    /dat.grid.connectionlist[0].area  /          dl_con_loc_xt_mtx_kgPm3   /mPmm/dayPs   # assuming connection area is a constant

#vel_liq_xt_mtx_mmPday    =  flo_liq_xt_mtx_mmPday*sl_con_loc_xt_mtx this does


#gas_flow_xt_mtx_kgPs              = -np.array([lst.history(('c',i,'FLO(GAS)'))[1] for i in lst.connection.row_name])
flo_gas_xt_mtx_kgPs       = -np.array([lst.history(('c',i,'FLO(GAS)'))[1] for i in lst.connection.row_name])
flo_gas_xt_mtx_mmPday     = flo_gas_xt_mtx_kgPs/dat.grid.connectionlist[0].area/dg_con_loc_xt_mtx_kgPm3/mPmm/dayPs

#vapor_diff_flow_xt_mtx_kgPs       = -np.array([lst.history(('c',i,'VAPDIF'))[1] for i in lst.connection.row_name])      # c means connection, but why negative? negative may related to BETAX, which is -1 in this case
#vapor_diff_flow_xt_mtx_mmPday     = vapor_diff_flow_xt_mtx_kgPs/dat.grid.connectionlist[0].area/dl_kgPm3/mPmm/dayPs
vap_dif_xt_mtx_kgPs       = -np.array([lst.history(('c',i,'VAPDIF'))[1] for i in lst.connection.row_name])      # c means connection, but why negative? negative may related to BETAX, which is -1 in this case
vap_dif_xt_mtx_mmPday     = vap_dif_xt_mtx_kgPs/dat.grid.connectionlist[0].area/    dv_sat_con_loc_xt_mtx_kgPm3    /mPmm/dayPs   # assuming connection area is a constant and vapor density
  
# gas_adv_velocity_mPs              = -1*np.array([lst.history(('c',lst.connection.row_name[i],'VEL(GAS)'))[1] for i in range(lst.connection.num_rows)])
# gas_adv_velocity_kgPs           = gas_adv_velocity_mPs*dg_kgPm3[1:]*dat.grid.connectionlist[0].area*dat.grid.rocktype['SAND '].porosity
# gas_adv_velocity_mmPday         = gas_adv_velocity_mPs*dat.grid.rocktype['SAND '].porosity/mPmm/dayPs 
# liquid_adv_velocity_mPs         = -1*np.array([lst.history(('c',lst.connection.row_name[i],'VEL(LIQ.)'))[1] for i in range(lst.connection.num_rows)])
# liquid_adv_velocity_kgPs        = liquid_adv_velocity_mPs*liq_density_kgPm3[1:]*dat.grid.connectionlist[0].area*dat.grid.rocktype['SAND '].porosity
# liquid_adv_velocity_mmPday      = liquid_adv_velocity_mPs*dat.grid.rocktype['SAND '].porosity/mPmm/dayPs 
# vap_adv_velocity_mmPday         = xairg_xt_mtx[1:]*gas_adv_velocity_mmPday
# vap_adv_velocity_kgPs           = xairg_xt_mtx[1:]*gas_adv_velocity_kgPs
# vap_adv_flow_top_mmPday         = vap_adv_velocity_mmPday[0]       
# vap_adv_flow_second_mmPday      = vap_adv_velocity_mmPday[1]
 
vap_adv_xt_mtx_mmPday     = xirg_xt_mtx[1:]*flo_gas_xt_mtx_mmPday
vap_adv_xt_mtx_kgPs       = xirg_xt_mtx[1:]*flo_gas_xt_mtx_kgPs


flo_liq_top_mmPday        = flo_liq_xt_mtx_mmPday[0]
flo_gas_top_mmPday        = flo_gas_xt_mtx_mmPday[0]
vap_adv_top_mmPday        = vap_adv_xt_mtx_mmPday[0]
vap_dif_top_mmPday        = vap_dif_xt_mtx_mmPday[0]


flo_liq_second_mmPday     = flo_liq_xt_mtx_mmPday[1]
flo_gas_second_mmPday     = flo_gas_xt_mtx_mmPday[1]
vap_adv_second_mmPday     = vap_adv_xt_mtx_mmPday[1]
vap_dif_second_mmPday     = vap_dif_xt_mtx_mmPday[1]

water_flow_top_mmPday       = flo_liq_top_mmPday+vap_adv_top_mmPday+vap_dif_top_mmPday
water_flow_second_mmPday    = flo_liq_second_mmPday+vap_adv_second_mmPday+vap_dif_second_mmPday

cumsum_water_flow_second_mm = np.cumsum(water_flow_second_mmPday*np.insert(np.diff(lst.times),0,lst.times[0])*dayPs)

water_generation_kgPs       = np.array([lst.history(('g',i,'GENERATION RATE'))[1] for i in lst.generation.row_name])
water_generation_mmPday     = water_generation_kgPs/dat.grid.connectionlist[0].area/liquid_density_kgPm3/mPmm/dayPs
#water_generation_vapor_mass_fraction    = np.array([lst.history(('g',i,'FF(GAS)' ))[1] for i in lst.generation.row_name])
#water_generation_liquid_mass_fraction   = np.array([lst.history(('g',i,'FF(LIQ.)'))[1] for i in lst.generation.row_name])  # what is FF(LIQ) mean and how did it distribute to both?
ff_gas   = np.array([lst.history(('g',i,'FF(GAS)' ))[1] for i in lst.generation.row_name])
ff_liq   = np.array([lst.history(('g',i,'FF(LIQ.)'))[1] for i in lst.generation.row_name])  # what is FF(LIQ) mean and how did it distribute to both?
water_generation_vapor_mmPday           = water_generation_mmPday*ff_gas
water_generation_liquid_mmPday          = water_generation_mmPday*ff_liq

#gas_relative_permeability               = np.array([lst.history(('p',lst.primary.row_name[i],'K(GAS)'))[1] for i in range(lst.primary.num_rows)])  TO 203004 what is primary
#liq_relative_permeability               = np.array([lst.history(('p',lst.primary.row_name[i],'K(LIQ.)'))[1] for i in range(lst.primary.num_rows)])

#gas_relative_permeability               = np.array([lst.history(('p',lst.connection.row_name[i],'K(GAS)'))[1] for i in  range(lst.connection.num_rows)])
#liq_relative_permeability               = np.array([lst.history(('p',lst.connection.row_name[i],'K(LIQ.)'))[1] for i in range(lst.connection.num_rows)])

# GAS_H                                   = np.array([lst.history(('p',lst.primary.row_name[i],'H(GAS)'))[1] for i in range(lst.primary.num_rows)])
# Liq_H                                   = np.array([lst.history(('p',lst.primary.row_name[i],'H(LIQ.)'))[1] for i in range(lst.primary.num_rows)])
# First_thermodynamic_change              = np.array([lst.history(('p',lst.primary.row_name[i],'DX1'))[1] for i in range(lst.primary.num_rows)])
# Second_thermodynamic_change             = np.array([lst.history(('p',lst.primary.row_name[i],'DX2'))[1] for i in range(lst.primary.num_rows)])
# Third_thermodynamic_change              = np.array([lst.history(('p',lst.primary.row_name[i],'DX3'))[1] for i in range(lst.primary.num_rows)])
# First_thermodynamic_var                 = np.array([lst.history(('p',lst.primary.row_name[i],'X1'))[1] for i in range(lst.primary.num_rows)])
# Second_thermodynamic_var                = np.array([lst.history(('p',lst.primary.row_name[i],'X2'))[1] for i in range(lst.primary.num_rows)])
# Third_thermodynamic_var                 = np.array([lst.history(('p',lst.primary.row_name[i],'X3'))[1] for i in range(lst.primary.num_rows)])

print('Parsing output file is completed.....\n')
