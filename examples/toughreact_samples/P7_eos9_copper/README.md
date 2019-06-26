### below is the result 

      -------- TOUGHREACT Version 2.0 ------- 

    --> reading multiphase flow input data      ->flow.inp
    --> reading solute transport input data     ->solute.inp
    --> reading chemical input data             ->chemical.inp therakin10.dat
    --> read input data complete

    --> performing simulation


  ...done! Toughreact v2.0 simulation finished





### required files
therakin10.dat
chemical.inp
flow.inp 
solute.inp


therakin10.dat             ! thermodynamic database
iter.dat                   ! iteration information    without this, the result may be different
Amic_aqu.dat               ! spatial distribution (tecplot format)
Amic_sod.dat               ! spatial distribution (tecplot format)
Amic_gas.dat               ! spatial distribution (tecplot format)
Amic_tim.dat               ! time evolution at specified blocks


### produced files
GENER 
INCON 
LINEQ 
MESH 
TABLE 
VERS
solute.out    
chemcal.out    -> simulation summary for chemical results



TO190624 compared this with the original output in TOUGHREACT samples




### useful commands
t2listing.fulltimes  -> the time (persumablly in seconds) of the output has been done
t2listing.times      -> same as t2listing.fulltimes
t2listing.fullsteps  -> the time steps that output has been done
t2listing.time       -> current time
t2listing.element.column_name  -> list of all output title elemental wise # ['PRES', 'S(liq)', 'PCAP', 'K(rel)', 'DIFFUS.']


