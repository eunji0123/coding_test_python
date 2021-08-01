# My solution
n, m = map(int, input().split())
x, y, d = map(int,input().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
maps[x][y] = 1

turn = 0
count = 1 # 처음 시작점도 방문한 곳이니까 count를 1부터 시작
while True:
    d = (d + 3) % 4
    turn += 1
    nx = x + dx[d]
    ny = y + dy[d]
    

    if maps[nx][ny] == 0:
        x, y = nx, ny
        maps[nx][ny] = 1 # 방문 처리(이때, 방문했든 바다이든 가지 못한다는 건 똑같으니까 같은 1로 처리)
        turn = 0 # turn을 다시 0으로 초기화
        count += 1
        continue

    if turn == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if maps[nx][ny] == 1:
            break
        x, y = nx, ny
        maps[nx][ny] = 1
        turn = 0
        count += 1

print(count)
