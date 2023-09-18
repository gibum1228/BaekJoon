import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    m = int(IN())
    cost = [-1 for _ in range(n+1)]
    G = [[] for _ in range(n+1)]

    # init graph
    for _ in range(m):
        s, e, distance = map(int, IN().split())

        G[s].append([e, distance])

    start, end = map(int, IN().split())

    # dijkstra
    que = []
    heapq.heappush(que, (0, start, [start]))
    cost[start] = 0
    results = []

    while que:
        distance, node, route = heapq.heappop(que)

        if -1 < cost[node] < distance: # 최소 거리 비용 업데이트가 불가능 하다면
            continue

        for (next_node, next_distance) in G[node]:
            weight = distance + next_distance

            if cost[next_node] == -1 or weight < cost[next_node]:
                cost[next_node] = weight
                next_route = route + [next_node]
                heapq.heappush(que, (weight, next_node, next_route))
                if next_node == end:
                    results = next_route

    print(cost[end])
    print(len(results))
    print(*results)