#!/usr/bin/env python

from mapper import getCentroids

def checkCentroidsDistance(centroids, centroids1):
    print("Centroids:", centroids)
    print("Centroids1:", centroids1)

    #check to ensure Centroids are being 
    if len(centroids) != 3 or len(centroids1) != 3:
        print("Error: Incorrect number of centroids")
        return

    #create distances list to determine if mapreduce should keep running
    distances = [
        (abs(centroids[i][0] - centroids1[i][0]) < 1 and
         abs(centroids[i][1] - centroids1[i][1]) < 1)
        for i in range(3)
    ]
    #depending on output continue or stop mapreduce
    if all(distances):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    try:
        centroids = getCentroids('centroids.txt')
        centroids1 = getCentroids('centroids1.txt')
    except Exception as e:
        print("Error reading centroids: {}".format(e))
        exit(1)

    checkCentroidsDistance(centroids, centroids1)