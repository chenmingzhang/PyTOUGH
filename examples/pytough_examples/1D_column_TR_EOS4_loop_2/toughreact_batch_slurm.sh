#!/bin/bash
## the right one we got is siD4.0e-10, siP5.0e-09, chD8.0e-10,  and pyD in 1.0e-06 

fn=Nature
ne="ne"
for siD in 4.0e-10 4.0e-08 4.0e-12 #siderite dissolution
do
    for siP in 5.0e-09 5.0e-07 5.0e-11  #siderite precipitation
    do
        for chD in 8.0e-09 8.0e-10 8.0e-11 #chlorite dissolution
        do
            for pyD in 1.0e-06  1.0e-07  1.0e-05 1.0e-04  #chlorite dissolution
            do
                #ddn=siD"$siD"siP"$siP"chD"$chD"pyD"$pyD"
                #ddn2=siD"$siD"siP"$siP"chD"$chD"pyD"$pyD"

                ddn=siD"${siD/.0e-/$ne}"_siP"${siP/.0e-/$ne}"_chD"${chD/.0e-/$ne}"_pyD"${pyD/.0e-/$ne}"
                ddn2=siD"${siD/.0e-/$ne}"_siP"${siP/.0e-/$ne}"_chD"${chD/.0e-/$ne}"_pyD"${pyD/.0e-/$ne}"

                echo $ddn
                #ddn2="$HY"E"$ET"S"$SY"P"$PU"
                #mkdir $ddn
                #cd    $ddn
                #                cp ../{"$fn".BAS, "$fn".DIS, "$fn".BCF, "$fn".EVT, \
                #                      "$fn".WEL "$fn".OC, "$fn".PCG, mf2k.nam} .
                #cp ../{"$fn".BAS,"$fn".DIS,"$fn".BCF,"$fn".EVT,"$fn".WEL,"$fn".OC,"$fn".PCG,mf2k.nam,job} .
                cp base_case $ddn -r
                cd $ddn
                sed -i s/namenamename/$ddn2/g      job.slurm
                sed -i s/sideriD/$siD/g    chemical.inp
        	    sed -i s/sideriP/$siP/g    chemical.inp
                sed -i s/chloriD/$chD/g    chemical.inp
                sed -i s/pyriteD/$pyD/g    chemical.inp
                sbatch job.slurm
                cd ..
                sleep 5
             done
        done
    done
done


