# A* Algorithm

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1), ('E', 5)],
    'C': [('F', 2)],
    'D': [('G', 4)],
    'E': [('G', 1)],
    'F': [('G', 1)],
    'G': []
}

# Heuristic values
h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 1,
    'F': 1,
    'G': 0
}

open_list = ['A']
closed_list = []
g = {'A': 0}
parent = {'A': 'A'}

goal = 'G'

while open_list:
    
    # Find node with lowest f(n)
    n = min(open_list, key=lambda x: g[x] + h[x])

    if n == goal:
        path = []
        while parent[n] != n:
            path.append(n)
            n = parent[n]
        path.append('A')
        path.reverse()

        print("Path found:", path)
        break

    open_list.remove(n)
    closed_list.append(n)

    for (m, cost) in graph[n]:
        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parent[m] = n
            g[m] = g[n] + cost
