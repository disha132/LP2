INF = 999

graph = [
    [0, 4, 0, 0, 8],
    [4, 0, 8, 0, 11],
    [0, 8, 0, 7, 2],
    [0, 0, 7, 0, 9],
    [8, 11, 2, 9, 0]
]

n = len(graph)

dist = [INF] * n
visited = [False] * n

dist[0] = 0

for _ in range(n):
    min_dist = INF

    for i in range(n):
        if not visited[i] and dist[i] < min_dist:
            min_dist = dist[i]
            u = i

    visited[u] = True

    for v in range(n):
        if graph[u][v] and not visited[v]:
            if dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

print("Shortest distances from source:")

for i in range(n):
    print("0 ->", i, "=", dist[i])
