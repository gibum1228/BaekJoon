import sys
import heapq


INF = 101


def dijkstra(X):
    # 우선순위 큐
    go_que = []
    back_que = []
    go_min_cost[X], back_min_cost[X] = 0, 0
    heapq.heappush(go_que, (0, X))
    heapq.heappush(back_que, (0, X))

    # 집에서 파티에 가는 최단 경로
    while go_que:
        g_distance, g_node = heapq.heappop(go_que)

        if g_distance <= go_min_cost[g_node]:
            for g_next in go_map[g_node]:
                g_weight = g_distance + g_next[0]

                if g_weight < go_min_cost[g_next[1]] or go_min_cost[g_next[1]] == INF:
                    go_min_cost[g_next[1]] = g_weight
                    heapq.heappush(go_que, (g_weight, g_next[1]))

    # 파티에서 집가는 최단 경로
    while back_que:
        b_distance, b_node = heapq.heappop(back_que)

        if b_distance <= back_min_cost[b_node]:
            for b_next in back_map[b_node]:
                b_weight = b_distance + b_next[0]

                if b_weight < back_min_cost[b_next[1]] or back_min_cost[b_next[1]] == INF:
                    back_min_cost[b_next[1]] = b_weight
                    heapq.heappush(back_que, (b_weight, b_next[1]))


if __name__ == "__main__":
    N, M, X = map(int, sys.stdin.readline().split())
    go_map = [[] for _ in range(N+1)]
    back_map = [[] for _ in range(N+1)]
    go_min_cost = [INF for _ in range(N+1)]
    back_min_cost = [INF for _ in range(N+1)]

    # input
    for i in range(M):
        A, B, T = map(int, sys.stdin.readline().split())

        go_map[A].append([T, B])
        back_map[B].append([T, A])

    # dijkstra
    dijkstra(X)

    # print
    weight = [0 for _ in range(N+1)]
    for i in range(1, N+1):
        weight[i] = go_min_cost[i] + back_min_cost[i]

    print(max(weight))