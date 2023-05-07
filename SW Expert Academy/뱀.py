"""
sol : 5.6.2023
리팩토링 필요
"""
# 3190 (뱀) : 구현
from collections import deque
n = int(input())
board = [[0] * n for _ in range(n)]
for _ in range(int(input())): # pos of apples
    i, j = map(int, input().split())
    board[i-1][j-1] = 5 # apple == 5

# 북, 동, 남, 서 : (0,1,2,3)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

direction = 1 # 초기엔 동쪽으로 이동
x, y = 0, 0 # 몸 시작 좌표

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3
    return direction

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0
    return direction

o = int(input()) # order 개수
order = []
for _ in range(o):
    sec, c = input().split()
    order.append((int(sec), c))

# HACK : YAGNI
# 구간합으로 입력된 sec와 다음 방향을 알려주는 c를 difference array와 현재 진행방향으로 변경
new_order = [(order[0][0], 1)] # 초기 진행은 오른쪽(1)
for i in range(o):
    if i < o - 1:
        diff = order[i+1][0] - order[i][0]
    else:
        diff = n
    if order[i][1] == 'D':
        dir = turn_right()
    else:
        dir = turn_left()
    new_order.append((diff, dir))
order = new_order

# 시뮬레이션 시작
result = 0 # 게임이 몇 초에 끝나는지
queue = deque() # 뱀 정보 담는 빈 큐
def solve():
    while order:
        sec, dir = order.pop(0)
        global x, y, result
        # sec만큼 dir 방향으로 이동.
        for _ in range(sec):
            result += 1
            nx = x + dx[dir] # 머리를 다음칸(nx, ny)에 위치
            ny = y + dy[dir]

            # 종료조건 1: 벽과 부딪치거나 (보드를 벗어날 경우)
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1:
                return result
            # 종료조건 2 : 자기 몸과 부딪치면
            if board[nx][ny] == 1:
                return result
        
            queue.append((nx, ny)) # 큐 오른쪽에 새 칸 추가
            # 사과가 있을 경우
            if board[nx][ny] == 5:
                board[nx][ny] = 0 # 사과 없어지고
                if (x, y) not in queue:
                    queue.appendleft((x, y)) # 큐 왼쪽에 몸 추가
            # 사과가 없을 경우
            else:
                tx, ty = queue.popleft() # 이전 칸 비우기
                board[tx][ty] = 0
            
            # 큐에 들어있는 뱀은 전부 방문처리
            for q in queue:
                qx, qy = q
                board[qx][qy] = 1

            x, y = nx, ny # 다음 위치는 현재 위치가 됨
       
solve()
print(result)
