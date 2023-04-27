# Union-Find
import sys
sys.setrecursionlimit(100000) # Runtime Error 날 경우, 재귀 limit 필요

# 1) 경로압축 find 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
  
# 2) 재귀 없이 while문으로 짜고 싶을 경우
def find_parent(x):
    while x != parent[x]:
        x = parent[x]
    return x

# 3) 일반적으로 사용되는 find 함수
def find_parent(x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]
  
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b
