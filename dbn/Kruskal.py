"""
Kruskal : MST(최소신장트리)의 일종
          가장 적은 비용으로 모든 노드를 연결
          간선의 개수가 E개일 때, O(ElogE) -> E개의 간선을 정렬하는데 ElogE시간이 걸리므로.
"""

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x] # here

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# Kruskal
v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
    parent[i] = i

edges = []
result = 0

for i in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클 발생 안 할 때
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
