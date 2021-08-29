# Good

from collections import deque

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int,input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    # 시작점을 방문 처리 하지 않아서 아래의 처음 방문하는 곳에 시작점도 포함되지만
    # 어차피 제일 마지막 노드만 중요하기 때문에 딱히 상관 없음.
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1:
                continue
            if maps[nx][ny] == 0:
                continue
            if maps[nx][ny] == 1: # 처음 방문하는 곳(시작점은 제외)
                queue.append((nx, ny))
                maps[nx][ny] = maps[x][y] + 1 # 말하자면 이게 방문 처리
    return maps[n-1][m-1]

print(bfs(0, 0))

    


    


