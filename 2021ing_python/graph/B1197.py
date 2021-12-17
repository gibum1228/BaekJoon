import sys


input = sys.stdin.readline


def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])

    return parent[v]


def union(a, b):
    root1 = find(a)
    root2 = find(b)
    parent[root2] = root1


def kruskal():
    result = 0
    edge = 0

    while True:
        if edge == V-1:
            break

        w, a, b = graph.pop(0)

        if find(a) != find(b):
            union(a, b)
            result += w
            edge += 1

    return result


if __name__ == "__main__":
    V, E = map(int, input().split())
    parent = [i for i in range(V+1)]
    graph = []

    # input graph
    for _ in range(E):
        A, B, C = map(int, input().split())

        graph.append((C, A, B)) # (가중치, 정점1, 정점2)
    graph.sort()

    print(kruskal())