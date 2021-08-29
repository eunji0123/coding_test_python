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

####################################################

# My solution 2 - Using DFS

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0

def dfs(v):
    graph[v[0]][v[1]] = 1
    for i in range(4):
        x = v[0] + dx[i]
        y = v[1] + dy[i]
        if x < 0 or x >= n or y < 0 or y >= m:
                continue
        if graph[x][y] == 0:
            dfs((x, y))

n, m = map(int, input().split())
graph = []

for _ in range(n):
    row = list(map(int, list(input())))
    graph.append(row)

#visited = [[False] * m for _ in range(n)]

for j in range(n):
    for k in range(m):
        if graph[j][k] == 0:
            dfs((j, k))
            count += 1

print(count)

####################################################

# test input
'''
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
'''
# test output : 8
