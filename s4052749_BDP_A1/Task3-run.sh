#!/bin/bash

# Define HDFS directories for input and output
INPUT_DIR="/Input"
INTERMEDIATE_DIR="/Task3process/intermediate"
OUTPUT_DIR="/Task3process/intermediatetwo"
OUTPUT_DIR2="/Output/Task3"

# Define local paths for mapper and reducer scripts
JOIN_MAPPER="/home/hadoop/joinMapperTU.py"
JOIN_REDUCER="/home/hadoop/joinReducerTU.py"
MAPPER2="/home/hadoop/Mapper2.py"
REDUCER2="/home/hadoop/Reducer2.py"
MAPPER3="/home/hadoop/Mapper3.py"
REDUCER3="/home/hadoop/Reducer3.py"


# Check if scripts exist
if [ ! -f $JOIN_MAPPER ]; then
    echo "Error: $JOIN_MAPPER does not exist."
    exit 1
fi

if [ ! -f $JOIN_REDUCER ]; then
    echo "Error: $JOIN_REDUCER does not exist."
    exit 1
fi

if [ ! -f $MAPPER2 ]; then
    echo "Error: $MAPPER2 does not exist."
    exit 1
fi

if [ ! -f $REDUCER2 ]; then
    echo "Error: $REDUCER2 does not exist."
    exit 1
fi

# Remove any existing output directories
hadoop fs -rm -r $OUTPUT_DIR
hadoop fs -rm -r $INTERMEDIATE_DIR
hadoop fs -rm -r $OUTPUT_DIR2

# Run the first MapReduce job
hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D stream.num.map.output.key.fields=1 \
    -D mapred.reduce.tasks=3 \
    -file $JOIN_MAPPER \
    -mapper $JOIN_MAPPER \
    -file $JOIN_REDUCER \
    -reducer $JOIN_REDUCER \
    -input $INPUT_DIR/*.txt \
    -output $INTERMEDIATE_DIR

# Check if the first job was successful
if [ $? -ne 0 ]; then
    echo "First MapReduce job failed."
    exit 1
fi

# Run the second MapReduce job using the output of the first job
hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D stream.num.map.output.key.fields=1 \
    -D mapred.reduce.tasks=3 \
    -file $MAPPER2 \
    -mapper $MAPPER2 \
    -file $REDUCER2 \
    -reducer $REDUCER2 \
    -input $INTERMEDIATE_DIR \
    -output $OUTPUT_DIR

# Check if the second job was successful
if [ $? -ne 0 ]; then
    echo "Second MapReduce job failed."
    exit 1
fi

# Run the second MapReduce job using the output of the first job
hadoop jar ./hadoop-streaming-3.1.4.jar \
    -D stream.num.map.output.key.fields=2 \
    -D mapred.text.key.partitioner.options=-k1,1 \
    -D mapred.reduce.tasks=3 \
    -file $MAPPER3 \
    -mapper $MAPPER3 \
    -file $REDUCER3 \
    -reducer $REDUCER3 \
    -input $OUTPUT_DIR \
    -output $OUTPUT_DIR2 \
    -partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


# Check if the third job was successful
if [ $? -ne 0 ]; then
    echo "Third MapReduce job failed."
    exit 1
fi


echo "all MapReduce jobs completed successfully."


# Run the second MapReduce job using the output of the first job
#hadoop jar ./hadoop-streaming-3.1.4.jar \
    #-D stream.map.output.field.separator=\t \
    #-D stream.num.map.output.key.fields=2 \
    #-D map.output.key.field.separator=\t \
    #-D mapred.text.key.partitioner.options=-k1,1 \
    #-D mapred.reduce.tasks=3 \
    #-file $MAPPER3 \
    #-mapper $MAPPER3 \
    #-file $REDUCER3 \
    #-reducer $REDUCER3 \
    #-input $OUTPUT_DIR \
    #-output $OUTPUT_DIR2 
    #-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner


