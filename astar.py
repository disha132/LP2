# A* Algorithm

graph = {
    'S': [('A', 1), ('B', 4)],
    'A': [('B', 2), ('C', 2),('D', 12)],
    'B': [('C', 2)],
    'C': [('D', 3)],
    'D': []
}

# Heuristic values
h = {
    'S': 7,
    'A': 6,
    'B': 2,
    'C': 1,
    'D': 0
}

open_list = ['S']
closed_list = []
g = {'S': 0}
parent = {'S': 'S'}

goal = 'D'

while open_list:
    
    # Find node with lowest f(n)
    n = min(open_list, key=lambda x: g[x] + h[x])

    if n == goal:
        path = []
        while parent[n] != n:
            path.append(n)
            n = parent[n]
        path.append('S')
        path.reverse()

        print("Path found:", path)
        break

    open_list.remove(n)
    closed_list.append(n)

    for (m, cost) in graph[n]:
        new_cost = g[n] + cost

        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parent[m] = n
            g[m] = new_cost

        elif new_cost < g.get(m, float('inf')):
            g[m] = new_cost
            parent[m] = n
