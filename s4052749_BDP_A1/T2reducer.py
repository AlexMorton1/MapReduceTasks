#!/usr/bin/env python

import sys

def calculateNewCentroids():
    current_centroid = None
    sum_x = 0
    sum_y = 0
    count = 0

    # Input comes from STDIN
    for line in sys.stdin:
        line = line.strip()
        parts = line.split('\t')
        
    
        if len(parts) != 3:
            continue

        centroid_index, x, y = parts
        
        
        # Convert x and y to float
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            continue
        
        # Check if we have a new centroid
        if current_centroid == centroid_index:
            count += 1
            sum_x += x
            sum_y += y


        else:
            #if current_centroid is not None:
            if count != 0:
                # Print the average of the previous centroid
                ave_x = (sum_x / count)
                ave_y = (sum_y / count)

                new_ave = "%s\t%s" % (ave_x, ave_y)
                print(new_ave)

            # Start processing the new centroid
            current_centroid = centroid_index
            sum_x = x
            sum_y = y
            count = 1

    
    # Print the last centroid's average
    if current_centroid is not None and count > 0:
    #if current_centroid == centroid_index and count != 0:
        ave_x = (sum_x / count)
        ave_y = (sum_y / count)

        new_ave = "%s\t%s" % (ave_x, ave_y)
        print(new_ave)

"""
"""

if __name__ == "__main__":
    calculateNewCentroids()