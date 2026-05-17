graph = [
    (0, 1, 2),
    (0, 3, 3),
    (0, 2, 6),
    (1, 3, 5),
    (2, 3, 4)
]

parent = [0, 1, 2, 3]

def find(x):
    while parent[x] != x:
        x = parent[x]
    return x

print("Edge : Weight")

for u, v, w in sorted(graph, key=lambda x: x[2]):
    pu = find(u)
    pv = find(v)

    if pu != pv:
        print(u, "-", v, ":", w)
        parent[pu] = pv
