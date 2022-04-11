# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem?isFullScreen=true



def mean(arr):
    return sum(arr)/len(arr)


    
def lin_reg(x, y, n):
    
    tot_x = sum(x)
    tot_y = sum(y)
    
    xsq = [i**2 for i in x]
    tot_xsq = sum(xsq)
    
    xy = [i*j for i, j in zip(x, y)]
    tot_xy = sum(xy)
    
    b = (n * tot_xy - tot_x * tot_y)/(n * tot_xsq - tot_x ** 2)
    a = mean(y) - b * mean(x)
    
    return a, b

    
def main():
    n = 5
    x, y = [0] * n, [0] * n

    for i in range(n):
        x[i], y[i] = map(int, input().split())

    a, b = lin_reg(x, y, n)

    result = a + b * 80
    print("{:.3f}".format(result))

    
if __name__ == "__main__":
    main()
