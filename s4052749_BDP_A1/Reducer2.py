#!/usr/bin/env python3
import sys

last_trip_Count = None
cur_company_Num = ""
current_count = 0

for line in sys.stdin:
    line = line.strip()
    
    try:
        company_Num, trip_Count = line.split("\t")
        trip_Count = int(trip_Count)  # Convert trip_Count to an integer
    except ValueError:
        print("Error parsing line:", line, file=sys.stderr)
        continue

    # If this is the first iteration
    if last_trip_Count is None:
        last_trip_Count = trip_Count
        cur_company_Num = company_Num
        current_count = trip_Count  # Start with the actual trip count

    # If the company_Num is the same as the current one, accumulate the count
    elif company_Num == cur_company_Num:
        current_count += trip_Count

    # Else, we have a new company_Num, so output the last one and reset for the new company_Num
    else:
        print('%s\t%s' % (cur_company_Num, current_count))
        cur_company_Num = company_Num
        current_count = trip_Count  # Start counting from this company's trip count

# Print out the last company_Num's total trip count
print('%s\t%s' % (cur_company_Num, current_count))