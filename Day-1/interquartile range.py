
# https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true

def median(lst):
    lst.sort()
    mid = len(lst) // 2
    if len(lst) % 2 != 0:
        return lst[mid]
    else:
        return (lst[mid] + lst[mid -1])/2
    
def interQuartile(values, freqs):
    
    ar = []
    for f, v in zip(freqs, values):
        for i in range(f):
            ar.append(v)
    ar.sort()
    
    mid = len(ar) // 2
    
    q1 = median(ar[0:mid])
    
    if len(ar) % 2 == 0:
        q3 = median(ar[mid:len(ar)])
    else:
        q3 = median(ar[mid + 1: len(ar)])
        
    res = float(q3 - q1)
    
    print(round(res, 1))