#!/bin/bash

hadoop fs -rm -r /Output/Task2*
cp initialization.txt centroids.txt 
cp initialization.txt centroids1.txt 

# Read the number of iterations from the initialization.txt file
iterations=$(head -n 1 initialization.txt)
i=1

while [ $i -le $iterations ]
do


    hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D mapred.reduce.tasks=3 \
    -D mapred.text.key.partitioner.options=-k1 \
    -file ./centroids.txt \
    -file ./T2mapper.py \
    -mapper ./T2mapper.py \
    -file ./T2reducer.py \
    -reducer ./T2reducer.py \
    -input /Input/Trips.txt \
    -output /Output/Task2/mapreduce-output$i \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

    # Remove old centroid1 file and get new one from Hadoop output
    rm -f centroids1.txt
    hadoop fs -getmerge /Output/Task2/mapreduce-output$i/ centroids1.txt
    
    # Use python script to check for termination condition
    seeiftrue=$(python reader.py)
    
    if [ "$seeiftrue" = "1" ]; then
        # If termination condition is met, break the loop
        rm centroids.txt
        cp centroids1.txt centroids.txt
        break
    else
        # Update the centroids for the next iteration
        rm centroids.txt
        cp centroids1.txt centroids.txt
    fi

    # Increment the loop counter
    i=$((i+1))
done