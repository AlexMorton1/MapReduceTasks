#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    try:
        company_Num, trip_Count = line.split("\t")

        if int(trip_Count) < 1000:
            print('%s\t%s\t%s' % (1, trip_Count, company_Num))

        elif int(trip_Count) < 1500:
            print('%s\t%s\t%s' % (2, trip_Count, company_Num))

        else:
            print('%s\t%s\t%s' % (3, trip_Count, company_Num))

    except ValueError:
        # Handle lines that don't split correctly
        print("Error processing line:", line, file=sys.stderr)