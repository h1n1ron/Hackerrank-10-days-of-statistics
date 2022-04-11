# https://www.hackerrank.com/challenges/s10-standard-deviation/problem?isFullScreen=true

import math

def stdDev(arr):
    def mean(data):
        return sum(data)/len(data)
    sdv = math.sqrt(sum([(arr[i] - mean(arr))**2 for i in range(len(arr))])/len(arr))
    print(round(sdv, 1))