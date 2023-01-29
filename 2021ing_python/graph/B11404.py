import sys
import heapq

IN = sys.stdin.readline
INF = float('inf')

if __name__ == "__main__":
    N = int(IN())
    G = {k: {} for k in range(1, N + 1)}

    for _ in range(int(IN())):
        a, b, c = map(int, IN().split())

        if G[a].get(b, -1) == -1:
            G[a][b] = c
        else:
            G[a][b] = min(G[a][b], c)


    def dijkstra(start_node):
        que = [(0, start_node)]
        distance = [INF for _ in range(N + 1)]
        distance[start_node] = 0

        while que:
            now_distance, now_node = heapq.heappop(que)

            for next_node, weight in G[now_node].items():
                next_distance = now_distance + weight

                if distance[next_node] <= next_distance:
                    continue
                else:
                    distance[next_node] = next_distance

                    heapq.heappush(que, (next_distance, next_node))

        for i in range(1, N + 1):
            if distance[i] == INF:
                print("0", end=" ")
            else:
                print(distance[i], end=" ")


    for i in range(1, N + 1):
        dijkstra(i)
        print()