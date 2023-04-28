# 구간 합 계산 Prefix_sum
# left 번째에서 right 번째까지 구간합을 알고 싶을 때
n = 5
data = [10, 20, 30, 40, 50]

sum_value = 0
prefix_sum = [0]
for i in data:
    sum_value += i
    prefix_sum.append(sum_value)

left = 3
right = 4
print(prefix_sum[right] - prefix_sum[left-1]) 

# Prefix_sum to difference Array
D = []
for i in range(n-1):
    D[i] = prefix_sum[i+1] - prefix_sum[i]
