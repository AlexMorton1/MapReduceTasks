#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    try:
        company_Num, trip_Count = line.split("\t")
        print('%s\t%s' % (company_Num, trip_Count))
    except ValueError:
        # Handle lines that don't split correctly
        print("Error processing line:", line, file=sys.stderr)