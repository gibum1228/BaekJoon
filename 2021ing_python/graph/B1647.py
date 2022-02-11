import sys
sys.setrecursionlimit(10**6)

IN = sys.stdin.readline

def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]

def union(a, b):
    root1 = find(a)
    root2 = find(b)
    if a < b:
        parent[root2] = root1
    else:
        parent[root1] = root2

def kruskal():
    result = 0
    edge = 0

    for w, a, b in board:
        if edge == N-2:
            break

        if find(a) != find(b):
            result += w
            edge += 1
            union(a, b)

    return result

if __name__ == "__main__":
    N, M = map(int, IN().split())
    parent = [i for i in range(N+1)]
    board = []

    for _ in range(M):
        A, B, C = map(int, IN().split())

        board.append([C, A, B])

    board.sort()

    print(kruskal())