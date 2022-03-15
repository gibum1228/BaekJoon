import sys
import copy

IN = sys.stdin.readline

def bfs(start):
    que = [start]
    next_que = []
    visited[start] = True
    R[start] = 0
    T[start] = 1
    R_count = 1
    T_count = 2

    while True:
        while que:
            focus_node = que.pop(0)

            for next_node in G[focus_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    next_que.append(next_node)
                    R[next_node] = R_count
                    T[next_node] = T_count
                    T_count += 1
        
        if next_que:
            que = copy.deepcopy(next_que)
            next_que = []
            R_count += 1
        else:
            return

if __name__ == "__main__":
    N, M, S = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    R = [-1 for _ in range(N+1)]
    T = [0 for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, IN().split())

        G[u].append(v)
        G[v].append(u)

    for i in range(1, N+1):
        G[i].sort()

    bfs(S)

    print(sum(list(map(lambda x, y: x * y, R, T))))