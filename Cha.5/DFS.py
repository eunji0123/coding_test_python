def dfs(graph, v, visited):
    # 방문 처리
    visited[v] = True
    print(v, end = ' ')
    # 인접 노드 처리
    for i in graph[v]:
        if not visited[i]: # 방문하지 않은 인접 노드일 경우
            dfs(graph, i, visited)

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

dfs(graph, 1, visited)

# graph와 visited를 꼭 dfs의 인수로 포함시킬 필요는 없음
    


