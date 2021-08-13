# My solution 1 - Using BFS

from collections import deque
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0

def bfs(start, n, m):
    queue = deque([start])
    #visited[start[0]][start[1]] = True
    graph[start[0]][start[1]] = 1
    while queue:
        v = queue.popleft()
        for i in range(4):
            x = v[0] + dx[i]
            y = v[1] + dy[i]
            if x < 0 or x >= n or y < 0 or y >= m:
                continue
            if graph[x][y] == 0:
                queue.append((x, y))
                graph[x][y] = 1
    

n, m = map(int, input().split())
graph = []

for _ in range(n):
    row = list(map(int, list(input())))
    graph.append(row)

#visited = [[False] * m for _ in range(n)]

for j in range(n):
    for k in range(m):
        if graph[j][k] == 0:
            bfs((j, k), n, m)
            count += 1

print(count)


