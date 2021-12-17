import sys

IN = sys.stdin.readline

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
        if edge == N-1:
            break

        w, a, b = board.pop(0)

        if find(a) != find(b):
            result += w
            edge += 1
            union(a, b)

    return result

if __name__ == "__main__":
    N = int(IN())
    M = int(IN())
    parent = [i for i in range(N+1)]
    board = []

    for i in range(M):
        A, B, C = map(int, IN().split())

        board.append((C, A, B))
    board.sort()

    print(kruskal())