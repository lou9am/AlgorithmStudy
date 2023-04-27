n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# Use DFS
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 아직 방문 안 한 노드면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1
print(result)
