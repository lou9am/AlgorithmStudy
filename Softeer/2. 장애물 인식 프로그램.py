# 지도 크기 입력받기
n = int(input())

visited = [[0] * n for _ in range(n)]
obs_num = 1

# 지도 정보 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# DFS
def dfs(x, y):
    # 지도 범위 벗어나면
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 1 이면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        visited[x][y] = obs_num
        # 상, 하, 좌, 우 재귀 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

obstacle = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            obstacle += 1
            obs_num += 1

print(obstacle)

count = []
for k in range(1, obstacle+1):
    cnt = 0
    for i in range(n):
        cnt += visited[i].count(k)
    count.append(cnt)
count.sort()
print(*count, sep='\n')
