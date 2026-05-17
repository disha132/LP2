INF = 999

graph = [
    [0, 2, 6, 3],
    [2, 0, 0, 5],
    [6, 0, 0, 4],
    [3, 5, 4, 0]
]

n = len(graph)

selected = [False] * n
selected[0] = True

print("Edge : Weight")

for _ in range(n - 1):
    minimum = INF

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if not selected[j] and graph[i][j]:
                    if graph[i][j] < minimum:
                        minimum = graph[i][j]
                        x, y = i, j

    print(x, "-", y, ":", graph[x][y])
    selected[y] = True
