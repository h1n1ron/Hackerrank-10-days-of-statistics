# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem?isFullScreen=true

import statistics as st

def pearson_coeff(n, dt_x, dt_y):
    x_bar = st.mean(dt_x)
    y_bar = st.mean(dt_y)
    sd_x = st.pstdev(dt_x)
    sd_y = st.pstdev(dt_y)
    
    c = 0
    
    for i in range(n):
        c += (dt_x[i] - x_bar) * (dt_y[i] - y_bar)
    return c / (n * sd_x * sd_y)


n = int(float(input()))
df_x = list(map(float, input().split()))
df_y = list(map(float, input().split()))

print(round(pearson_coeff(n, df_x, df_y), 3))