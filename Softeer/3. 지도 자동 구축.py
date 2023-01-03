import sys

n = int(input())

# DP Table
d = [0] * (n+1)
d[0] = 4

for i in range(1, n+1):
    d[i] = 2*(d[i-1]-1)

result = d[n-1] * 2 ** n + 1
print(result)
