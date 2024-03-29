n, m = map(int, input().split())

# 방문한 위치 저장하는 맵
check = [[0] * m for _ in range(n)]

x, y, direction = map(int, input().split())
check[x][y] = 1

# map
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# main
count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    if check[nx][ny] == 0 and array[nx][ny] == 0:
        check[nx][ny] = 1
        x, y = nx, ny
        count += 1
        turn_time = 0
        continue # 아래 코드 전부 실행 안하고 while문 반복

    else:
        turn_time += 1
    
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:
            x = nx
            y = ny
        else : 
            break
        turn_time = 0

print(count)
