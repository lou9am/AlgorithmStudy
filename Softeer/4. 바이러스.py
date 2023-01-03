import sys

k, p, n = map(int, input().split())

for i in range(n):
    k *= p
    k %= 1000000007

print(k)
