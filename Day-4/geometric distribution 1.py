# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem?isFullScreen=true

num = list(map(int, input().split()))

p = num[0]/num[1]
n = int(input())
print(round(((1-p)**(n - 1)) * p, 3))