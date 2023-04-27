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
