#!/usr/bin/env python

import sys
from math import sqrt

# get initial centroids from a txt file and add them in an array
def getCentroids(filepath):
    centroids = []

    with open(filepath) as fp:
        line = fp.readline()
        while line:
            if line:
                line = line.strip()
                cord = line.split('\t')
                #check line isn't K if not append row to centroids
                if len(cord) > 1:
                    try:
                        centroids.append([float(cord[0]), float(cord[1])]) 

                    except:
                        break
            else: 
                break
            line = fp.readline()

    fp.close()
    return centroids

# create clusters based on initial centroids
def createClusters(centroids):
    # 
    for line in sys.stdin:
        line = line.strip()
        cord = line.split(',')
        min_dist = 100000000000000
        index = -1

        for centroid in centroids:

            try:
                cord[6] = float(cord[6])
                cord[7] = float(cord[7])
            except ValueError:
                # float was not a number, so silently
                # ignore/discard this line
                continue

            # euclidian distance from every point of dataset
            # to every centroid
            cur_dist = sqrt(pow(cord[6] - centroid[0], 2) + pow(cord[7] - centroid[1], 2))
            cur_dist = float(cur_dist)


            # find the centroid which is closer to the point
            if cur_dist <= min_dist:
                min_dist = cur_dist
                index = centroids.index(centroid)

        var = "%s\t%s\t%s" % (index, cord[6], cord[7])
        print(var)

if __name__ == "__main__":
    centroids = getCentroids('centroids.txt')
    #print(centroids)
    createClusters(centroids)