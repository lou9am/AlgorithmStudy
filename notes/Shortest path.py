"""
Dijkstra, Floyd-Warshall 등 최단경로 문제를 풀 때 주의해야할 점(a.k.a #9370 틀린 이유)

1) 최단 경로는 반드시 하나만 존재하는 것이 아니다.

같은 cost를 갖는 경로가 여러 개 존재할 수 있기 때문에 "최단 경로가 특정 경로를 지나가는가"를 알고 싶을 때
최단 경로를 역추적한 후, 경로 상에 특정 경로 존재 여부를 찾는 것은 옳은 로직이 아니다.

출발지 -> 특정경로
특정경로 -> 도착지

까지의 cost합이 최단 경로 cost와 같은지 비교해야 옳은 로직이다.
"""
# BOj 9370 미확인 도착지
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
            
    return distance[end] - distance[start]

for _ in range(int(input())):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    ans = []
    for _ in range(t):
        x = int(input())
        s_to_g = dijkstra(s, g)
        g_to_h = dijkstra(g, h)
        h_to_x = dijkstra(h, x)

        s_to_h = dijkstra(s, h)
        h_to_g = dijkstra(h, g)
        g_to_x = dijkstra(g, x)
        
        if s_to_g + g_to_h + h_to_x == dijkstra(s, x) or s_to_h + h_to_g + g_to_x == dijkstra(s, x):
            ans.append(x)        
        
    ans.sort()
    print(' '.join(map(str,ans)))
