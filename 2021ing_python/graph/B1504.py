import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    N, E = map(int, IN().split())
    # 그래프 입력 받기
    graph = {i:dict() for i in range(1, N+1)}
    for _ in range(E):
        a, b, c = map(int, IN().split())
        graph[a][b] = c
        graph[b][a] = c
    # 지나가야 하는 두 개의 정점
    v1, v2 = map(int, IN().split())

    def dijkstra(graph, start):
        # 최단 거리를 저장하는 딕셔너리
        distance = {i: float('inf') for i in range(1, N+1)}
        distance[start] = 0
        # 우선순위 큐
        que = []
        heapq.heappush(que, (start, distance[start]))

        while que:
            current_node, current_distance = heapq.heappop(que)

            # 기록된 거리가 더 최단거리면 무시
            if distance[current_node] < current_distance:
                continue

            for next_node, next_distance in graph[current_node].items():
                if_distance = current_distance + next_distance

                if if_distance < distance[next_node]:
                    distance[next_node] = if_distance
                    heapq.heappush(que, (next_node, if_distance))

        return distance

    # 조건에 부합하려면 두 가지 경우가 있음 -> 1-v1-v2-N or 1-v2-v1-N
    one_dist = dijkstra(graph, 1)
    v1_dist = dijkstra(graph, v1)
    v2_dist = dijkstra(graph, v2)
    # 정답 확인
    result = min(one_dist[v1] + v1_dist[v2] + v2_dist[N], one_dist[v2] + v2_dist[v1] + v1_dist[N])
    print(result if result < float('inf') else -1)