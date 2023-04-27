# 투 포인터
# 1. 특정한 값을 가지는 부분 연속 수열 찾기
# 단, 음수 데이터가 포함되어 있는 경우 투 포인터로 해결 불가

n = 5 # 데이터 개수
m = 5 # 찾고자 하는 부분합
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

# start를 차례대로 증가시키며 반복
for start in range(n):
    # end를 가능한 만큼 이동시키기
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    # 부분합이 m일 때 카운트 증가
    if interval_sum == m:
        count += 1
    interval_sum -= data[start]

print(count)


# 2. 정렬되어 있는 두 리스트의 합집합
# 각 리스트의 원소 개수가 n,m일 때 O(n+m)
n, m = 3, 4
a = [1,3,5]
b = [2,4,6,8]

result = [0] * (n+m)
i = 0 # 리스트 a
j = 0 # 리스트 b
k = 0 # 결과 리스트

# 모든 원소가 결과 리스트에 담길 때까지 반복
while i < n or j < m:
    # 리스트 b의 모든 원소가 처리되었거나, 리스트 a의 원소가 더 작을 때
    if j >= m or (i < n and a[i] <= b[j]):
        result[k] = a[i]
        i += 1
    # 리스트 a의 모든 원소가 처리되었거나, 리스트 b의 원소가 더 작을 때
    else:
        result[k] = b[j]
        j += 1
    k += 1

for i in result:
    print(i, end='')
    
# 2번의 경우, 시간이 오래 걸리므로 그냥 두 리스트를 더한 다음에 quick sort로 정렬하는 것이 빠름
