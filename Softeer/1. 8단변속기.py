import sys

data = list(map(int, input().split()))

ascending = [1,2,3,4,5,6,7,8]
decending = [8,7,6,5,4,3,2,1]

if data == ascending:
    print('ascending')
elif data == decending:
    print('descending')
else:
    print('mixed')
