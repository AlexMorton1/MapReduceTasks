#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()  # Remove leading and trailing whitespaces

    taxi_Num = "" 
    company_Num = float("inf")
    trip_Count = 0

    line = line.split(",")
    
    #assign variable depending on document input
    if len(line) == 4: 
        taxi_Num = line[0]
        company_Num = line[1]

    else: 
        taxi_Num = line[1]
        trip_Count = 1   
    

    # Write the result to the output file
    print('%s\t%s\t%s' % (taxi_Num,company_Num,trip_Count))