# https://www.hackerrank.com/challenges/s10-weighted-mean/problem?isFullScreen=true

def weightedMean(X, W):
    
    print(round(sum([X[i]*W[i] for i in range(len(X))])/sum(W), 1))