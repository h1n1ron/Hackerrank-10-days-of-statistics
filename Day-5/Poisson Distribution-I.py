# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem?isFullScreen=true
import math

def poisson(k, lam):
    return(math.exp(-lam)*(lam**k)/math.factorial(k))
    
lam = float(input())
k = int(input())

print(round(poisson(k, lam), 3))