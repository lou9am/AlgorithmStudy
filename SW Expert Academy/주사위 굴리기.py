n, m, x, y, k = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int,input().split())))
order = list(map(int, input().split())) # k개의 명령

# 0, 1, 2, 3, 4, 5
dice = [0, 0, 0, 0, 0, 0] # 전개도 순서대로 위, 북, 동, 서, 남, 아래

# 명령어 동, 서, 북, 남 : 1, 2, 3, 4
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

# HACK : DRY해서 좀 더 간단한 수식으로 바꿀 예정
def roll_dice(dir):
    global dice
    bottom = dice[5]
    if dir == 1: # 동쪽 이동 (남, 북은 변경 없음)
        dice[5] = dice[2] # 동쪽이 아래 2->5
        dice[2] = dice[0] # 위가 동쪽 0->2
        dice[0] = dice[3] # 서쪽이 위 3->0
        dice[3] = bottom # 아래는 서쪽 5->3
    elif dir == 2: # 서쪽 이동 (남, 북은 변경 없음)
        dice[5] = dice[3] # 서쪽이 아래 3->5
        dice[3] = dice[0] # 위가 서쪽 0->3
        dice[0] = dice[2] # 동쪽이 위 2->0
        dice[2] = bottom # 아래는 동쪽 5->2
    elif dir == 3: # 북쪽 이동 (동, 서는 변경 없음)
        dice[5] = dice[1] # 아래에 북이 들어옴
        dice[1] = dice[0] # 북에 위가 들어옴
        dice[0] = dice[4] # 위에 남이 들어옴
        dice[4] = bottom # 남에 아래가 들어옴
    else: # 남쪽 이동 (동, 서는 변경 없음)
        dice[5] = dice[4] # 아래에 북이 들어옴
        dice[4] = dice[0] # 북에 위가 들어옴
        dice[0] = dice[1] # 위에 남이 들어옴
        dice[1] = bottom # 남에 아래가 들어옴
        

while order:
    dir = order.pop(0)
    nx = x + dx[dir]
    ny = y + dy[dir]

    # 바깥으로 이동하려 하면 무시
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

    roll_dice(dir)

    # 지도가 0이면 지도가 주사위 바닥면 숫자로 바뀜
    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    # 0이 아니면 지도 숫자가 주사위 바닥면으로 이동, 칸에 있던 숫자는 0됨
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    
    x, y = nx, ny
    print(dice[0]) # 윗면 출력
