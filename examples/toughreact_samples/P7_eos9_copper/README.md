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



TO190624 compared this with the original output in TOUGHREACT samples
