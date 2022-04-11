# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem?isFullScreen=true
a = list(map(float, input().split(" ")))

b = a[0]
c = a[1]

ca = 160 + 40 * (b + b**2)
cb = 128 + 40 * (c + c**2)

print(round(ca, 3))
print(round(cb, 3))