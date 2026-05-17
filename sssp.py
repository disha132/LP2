import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0

    pq = [(0, start)]   # (distance, node)

    while pq:
        d, u = heapq.heappop(pq)

        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


# Graph representation
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start = 0

result = dijkstra(graph, start)

print("Shortest distances from source node", start)
for i in range(len(result)):
    print(f"To node {i} = {result[i]}")
