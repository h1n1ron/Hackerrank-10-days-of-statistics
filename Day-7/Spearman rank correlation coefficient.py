# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient?isFullScreen=true

def spearman_coeff(n, x, y):
    
    diff_sq = [(i - j) ** 2 for (i, j) in zip(x, y)]
    coeff = 1 - (6 * sum(diff_sq)) / (n**3 - n)
    return coeff

n = int(input())
X = [float(x) for x in input().split()]
Y = [float(x) for x in input().split()]

X_rank = [sorted(X).index(x) + 1 for x in X]
Y_rank = [sorted(Y).index(y) + 1 for y in Y]


print(round(spearman_coeff(n, X_rank, Y_rank), 3))