#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespaces
    
    

    tripNum, taxiNum, fare, distance, pickup_x, pickup_y, dropoff_x, dropoff_y = line.split(",")  # Split the line into words and returns as a list
    
    distance = float(distance)  # Convert distance to float
    
    # Determine the distance category
    if distance < 100:
        distanceCat = "short"
    elif 100 <= distance < 200:
        distanceCat = "medium"
    else:
        distanceCat = "long"
    
    
    # Create the taxi number with distance category
    taxiNumDist = taxiNum+"-"+distanceCat

    # Write the result to the output file
    print('%s\t%s\t%s' % (taxiNumDist,fare,1))