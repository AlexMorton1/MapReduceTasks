#!/usr/bin/env python3
import sys

# Set dummy variables
last_taxi_num = None
cur_company = "_"
total_trip_count = 0

# Read in and trim input from stdin
for line in sys.stdin:
    line = line.strip()
    taxi_num, company_num, trip_count = line.split("\t")

    # Convert trip_count to integer for accumulation
    trip_count = int(trip_count)

    if company_num != 'inf': 
        cur_company = company_num

    if last_taxi_num == taxi_num:
        # Accumulate trip counts for the same taxi number
        total_trip_count += trip_count

    else:
        # Print the previous taxi's data if not the first record
        if last_taxi_num is not None:
            print(f'{cur_company}\t{total_trip_count}')
        
        # Update to the new taxi number
        last_taxi_num = taxi_num
        cur_company = company_num
        total_trip_count = trip_count

# Print the last taxi's data
if last_taxi_num is not None:
    print(f'{cur_company}\t{total_trip_count}')