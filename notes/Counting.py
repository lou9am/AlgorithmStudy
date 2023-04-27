# 원소의 개수를 세는 여러 방법들

# 1. Counter
# 장점 : 내장 라이브러리 사용으로 간편하게 구현 가능
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green'])
print(counter['blue']) # 1
print(counter['red']) # 2

# 2. bisect
# 정렬된 리스트에서 범위 안의 원소 개수 셀 때 유용
from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index
  
# 3. Set
# 원소의 종류만 셀 때는 집합 자료형이 유용.
# 집합은 중복을 허용하지 않으므로 특정 원소가 존재하는지만 검사하거나 등장 여부 체크할 때는 in 대신 set이 O(1)로 더 빠름
array = [1, 2, 3, 4, 5, 5, 5, 3, 1]
tmp = set(array)
print(tmp) # 1, 2, 3, 4, 5

# 3이 array안에 존재하는지 확인
for i in range(len(array)): # in은 순차탐색이므로 O(n) 소요
    if array[i] == 3:
        print('YES')
        break

print("YES" if 3 in set(array) else "NO") # O(1) 소요

# 4. 그 외
# python에서 원소 개수를 counting 해주는 방식이 여럿 존재하므로, 전통적인 방법으로 순차탐색 하며 in 함수를 쓰는 것은 지양할 것. 시간초과나기 쉬움.
