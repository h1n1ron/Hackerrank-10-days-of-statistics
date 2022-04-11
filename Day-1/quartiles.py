
# https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true

def median(lst):
    lst.sort()
    mid = len(lst) // 2
    if len(lst) % 2 != 0:
        return lst[mid]
    else:
        return (lst[mid] + lst[mid -1])/2

        
def quartiles(arr):
    q2 = median(arr)
    
    n = len(arr)
    mid = len(arr) // 2
    
    if n % 2 != 0:
        q1 = median(arr[0:mid])
        q3 = median(arr[(mid + 1):n])
    else:
        q1 = median(arr[0:mid])
        q3 = median(arr[mid:n])
    return [int(x) for x in [q1, q2, q3]]
    