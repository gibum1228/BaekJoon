import sys
import copy

IN = sys.stdin.readline

def bfs(start):
    que = [start]
    next_que = []
    visited[start] = True
    results[start] = 0
    count = 1

    while True:
        while que:
            focus_node = que.pop(0)

            for next_node in G[focus_node]:
                if not visited[next_node]:
                    visited[next_node] = True
                    next_que.append(next_node)
                    results[next_node] = count
        
        if next_que:
            que = copy.deepcopy(next_que)
            next_que = []
            count += 1
        else:
            return

if __name__ == "__main__":
    N, M, R = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    results = [-1 for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, IN().split())

        G[u].append(v)
        G[v].append(u)

    bfs(R)
    
    print("\n".join(map(str, results[1:])))