import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    weight = [0] * (N+1)
    weight[0] = -1
    graph = [[] for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M):
        A, B = map(int, IN().split())

        graph[A].append(B)
        weight[B] += 1

    def bfs():
        que = []
        result = []

        try:
            while True:
                index = weight.index(0)

                if not visited[index]:
                    visited[index] = True
                    que.append(index)
                    result.append(index)
                    weight[index] = -1

                    for next in graph[index]:
                        weight[next] -= 1
        except:
            pass

        return result

    print(" ".join(list(map(str, bfs()))))