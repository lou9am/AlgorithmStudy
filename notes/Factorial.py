"""
팩토리얼을 구현하는 3가지 방법
"""

# 1. Pythonic하게 삼항연산자 사용
def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

# 2. 재귀 호출
def factorial(n):
    if n > 1:
        return n * factorial(n-1)
    else:
        return 1

# 3. DP 사용
def dp_factorial(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1, n+1):
        dp[i] = dp[i-1] * i
    return dp[n]
