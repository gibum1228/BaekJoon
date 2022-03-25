import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    M = int(IN())
    G = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    results = len(G[1])

    for _ in range(M):
        a, b = map(int, IN().split())

        G[a].append(b)
        G[b].append(a)
    
    def bfs():
        global results

        for x in G[1]:
            visited[x] = True

            for i in G[x]:
                if not visited[i]:
                    visited[i] = True
                    results += 1

    bfs()

    print(results)