from collections import deque

def bfs(graph, start, visited):
    # 시작 노드 큐에 삽입하고 방문 처리
    queue = deque([start])
    visited[start] = True
    while queue: # 큐가 빌 때까지 반복
        # 큐에서 제일 첫 노드 꺼내서 출력
        v = queue.popleft()
        print(v, end = ' ')
        # 그 노드의 인접노드 중 방문하지 않은 노드
        # 큐에 삽입하고 방문 처리
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                

graph = [[],
         [2, 3, 8],
         [1, 7],
         [1, 4, 5],
         [3, 5],
         [3, 4],
         [7],
         [2, 6, 8],
         [1, 7]]
visited = [False] * 9


bfs(graph, 1, visited)
