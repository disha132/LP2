from collections import deque

graph = {}
visited =set()

def dfs(v):
    visited.add(v)
    print(v,end=" ")

    for i in graph[v]:
        if i not in visited:
            dfs(i)

def bfs(start):
    q = deque([start])
    visited.add(start)

    while q:
        v= q.popleft()
        print(v, end=" ")

        for i in graph[v]:
            if i not in visited:
                visited.add(i)
                q.append(i)


n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))

for i in range(n):
    graph[i] = []

print("Enter Edges: ")
for i in range(e):
    u,v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


while True:
    visited.clear()

    print("\n 1. DFS")
    print("2. BFS")
    print("3. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        start = int(input("Enter starting vertex: "))
        print("DFS Traversal:")
        dfs(start)

    elif ch == 2:
        start = int(input("Enter starting vertex: "))
        print("BFS Traversal:")
        bfs(start)

    elif ch == 3:
        print("Exiting...")
        break

    else:
        print("Invalid Choice")