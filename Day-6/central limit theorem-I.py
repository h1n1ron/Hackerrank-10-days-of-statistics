# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem?isFullScreen=true
import math
weight = int(input())
amount = int(input())
mu = int(input())
sd = int(input())

print(round(0.5 * (1 + math.erf((weight - mu*amount) / (sd*math.sqrt(amount) * (2 ** 0.5)))), 4))