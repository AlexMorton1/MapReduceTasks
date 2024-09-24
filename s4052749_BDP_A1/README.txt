
# Copying the input files to HDFS root dir from my current working dir
hadoop fs -mkdir /Input
hadoop fs -put Trips.txt /Input/
hadoop fs -put Taxis.txt /Input/
hadoop fs -ls /Input

################################################################
# Remove all Output dirs on HDFS
hadoop fs -rm -r /Output
# unzip student submission zip 
# Copying the streaming jar to the current working dir
# Copying the "initialization.txt" (for task2) to the current working dir

################################################################
# Run task 1
./Task1-run.sh
# copy the task 1 output to the current dir
hadoop fs –getmerge /Output/Task1/ Task1_output.txt
# check the total number of records in the output
# sort on (taxi#, trip_type) and display the first 10 records
# sort on (taxi#, trip_type) and display the last 10 records

################################################################
copy the following commands into the terminal 
cp initialization.txt centroids.txt
cp initialization.txt centroids1.txt
# Run task 2
./Task2-run.sh
# copy the task 2 output to the current dir
# out is done by automatically by Task2-run.sh but can be re compiled as centroids.txt 
# but can also be gathered using the following command
hadoop fs –getmerge /Output/Task2/mapreduce-output10/ Task2_output.txt 
# check the medoids generated

################################################################
# Run task 3
./Task3-run.sh
# copy the task 3 output to the current dir
hadoop fs -getmerge /Output/Task3/ Task3_output.txt 
# check the total number of records in the output 
# display the first 10 records
# display the last 10 records



