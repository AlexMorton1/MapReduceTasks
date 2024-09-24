#!/usr/bin/env python3
import sys 

    # Iterate over each line of reducer input
for line in sys.stdin:
    try: 
        index, trip_Count, company_Num = line.strip().split("\t")
        print('%s\t%s\t%s' % (index, trip_Count, company_Num))


    except ValueError:
        # Handle lines that don't split correctly
        print("Error processing line:", line, file=sys.stderr)

