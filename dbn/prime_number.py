# prime number
"""
소수인지 확인하기 위해서는 가운데 약수까지만 나누어 떨어지는지 확인하면 된다.
"""
import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

print(is_prime_number(4)) # False
print(is_prime_number(7)) # True


# 에라토스테네스의 체 : 여러 개의 수가 소수인지 아닌지 판별
# 단점 : 메모리를 많이 요구함. N이 1,000,000 이내로 주어질 때만 사용.
# 1이 소수인지 판별해야 할 경우, array[1] = False 추가
"""
1. 2~N 까지의 모든 자연수를 나열
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다. (i는 제거하지 않는다.)
4. 더 이상 반복할 수 없을 때까지 2~3을 반복한다.
"""
import math
n = 100
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True: # i가 남은 수(소수)인 경우
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1
# 모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end= ' ')
