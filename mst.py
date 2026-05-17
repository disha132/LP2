# Prim's Algorithm for Minimum Spanning Tree

INF = 9999999

# Number of vertices
n = 5

# Graph represented using adjacency matrix
G = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]

selected = [0] * n

# Start from first vertex
selected[0] = True

print("Edge : Weight\n")

no_edge = 0

while no_edge < n - 1:

    minimum = INF
    x = 0
    y = 0

    for i in range(n):
        if selected[i]:
            for j in range(n):
                if (not selected[j]) and G[i][j]:

                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j

    print(x, "-", y, ":", G[x][y])

    selected[y] = True
    no_edge += 1
