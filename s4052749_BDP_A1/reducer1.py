#!/usr/bin/env python3
import sys

# Initialize variables
current_taxi_num_type = None
trip_count = 0
max_fare = float('-inf')
min_fare = float('inf')
total_fare = 0.0

# Read input from STDIN
for line in sys.stdin:
    # Remove leading/trailing whitespace
    line = line.strip()

    # Parse the input we got from mapper
    taxi_num_trip_type, fare, n = line.split('\t')
    fare = float(fare)

    # Check if we are still processing the same key (taxi_trip_type)
    if current_taxi_num_type == taxi_num_trip_type:
        trip_count += 1
        total_fare += fare
        max_fare = max(max_fare, fare)
        min_fare = min(min_fare, fare)
    else:
        # If the key has changed and it's not the first key
        if current_taxi_num_type:
            # Output the result for the previous key
            average_fare = total_fare / trip_count
            print(f"{current_taxi_num_type}\t{trip_count}\t{round(max_fare, 2)}\t{round(min_fare,2)}\t{round(average_fare, 2)}")

        # Reset variables for the new key
        current_taxi_num_type = taxi_num_trip_type
        trip_count = 1
        total_fare = fare
        max_fare = fare
        min_fare = fare

# Output the result for the last key
if current_taxi_num_type == taxi_num_trip_type:
    average_fare = total_fare / trip_count
    print(f"{current_taxi_num_type}\t{trip_count}\t{round(max_fare, 2)}\t{round(min_fare,2)}\t{round(average_fare, 2)}")