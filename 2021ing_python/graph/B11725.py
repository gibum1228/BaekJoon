import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    G = {i: set([]) for i in range(1, N+1)}
    result = {}

    for _ in range(N-1):
        a, b = map(int, IN().split())

        G[a].add(b)
        G[b].add(a)

    visited, que = [False for __ in range(N+1)], deque([(1, 1)])
    while que:
        parents, child = que.popleft()
        result[child] = parents

        for childchild in G[child]:
            if not visited[childchild]:
                visited[childchild] = True
                que.append((child, childchild))

    s = ""
    for i in range(2, N+1):
        s += str(result[i]) + "\n"
    print(s)