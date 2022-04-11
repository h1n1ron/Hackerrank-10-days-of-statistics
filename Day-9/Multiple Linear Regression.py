# https://www.hackerrank.com/challenges/s10-multiple-linear-regression/problem?isFullScreen=true




import numpy as np


def ls(x, y):
    a = np.append(x, np.ones((len(x), 1)), axis=-1)
    y = y[:, np.newaxis]

    result = np.linalg.inv(np.dot(a.T, a))
    result = np.dot(result, a.T)
    result = np.dot(result, y)

    return result[-1][0], result[:-1]


def main():

    m, n = list(map(int, str.split(input(), " ")))
    data = [list(float(x) for x in input().split()) for i in range(n)]

    x = np.array([[item[i] for i in range(m)] for item in data])
    y = np.array([item[-1] for item in data])

    a, b = ls(x, y)

    q = int(input())

    for i in range(q):
        data = list(map(float, input().split()))
        result = [b[j] * data[j] for j in range(m)]
        result = a + np.sum(result)
        print("{:.3f}".format(result))


if __name__ == "__main__":
    main()