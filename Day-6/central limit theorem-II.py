# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-2/problem?isFullScreen=true

import math

def cdf(sd, mu, x):
    Fx = 1 + math.erf((x -mu) / (sd * math.sqrt(2)))
    return Fx * 0.5


max_weight = float(input())
n = float(input())
mean = float(input())
std = float(input())

new_mean  = mean * n
new_std = math.sqrt(n) * std

print(round(cdf(new_std, new_mean, max_weight), 4))