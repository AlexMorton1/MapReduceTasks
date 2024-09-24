#!/bin/bash
hadoop fs -rm -r /Output/Task1*
    
hadoop jar ./hadoop-streaming-3.1.4.jar \
-D stream.num.map.output.key.fields=1 \
-D mapred.reduce.tasks=3 \
-file ./mapper1.py \
-mapper ./mapper1.py \
-file ./reducer1.py \
-reducer ./reducer1.py \
-input /Input/Trips.txt \
-output /Output/Task1

