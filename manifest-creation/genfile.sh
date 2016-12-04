#!/bin/bash 

for (( i=0; i<$2; i+=$1 )) 
do 
	python create_manifest.py $i $(($i+$1)) $3 >> $4"_manifest_"$i"-"$(($i+$1))".json"
done 
