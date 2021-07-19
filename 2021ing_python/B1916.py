import sys
import heapq

# 다익스트라 알고리즘
def dijkstra(start):
    que = [] # 우선순위 큐
    # init
    heapq.heappush(que, (0, start))
    cost[start] = 0

    # 우선순위 큐가 빌 때까지 반복
    while que:
        distance, city = heapq.heappop(que) # 현재 city와 거리를 가져옴

        # 현재 거리보다 현재 city를 최소 비용으로 갈 수 있는 방법이 있다면
        if -1 < cost[city] < distance:
            continue

        for next in graph[city]:
            weight = distance + next[1] # 현재 city를 걸치고 next[0]로 가는 비용

            # 현재 알고 있는 최소 비용을 업데이트 할 수 있다면
            if weight < cost[next[0]] or cost[next[0]] == -1:
                cost[next[0]] = weight
                heapq.heappush(que, (weight, next[0])) # 우선순위 큐에 추가

if __name__ == '__main__':
    city_count = int(sys.stdin.readline())
    bus_count = int(sys.stdin.readline())
    cost = [-1 for _ in range(city_count + 1)] # 최소 비용을 담는 리스트

    # graph input
    graph = [[] for _ in range(city_count + 1)]
    for _ in range(bus_count):
        s, e, w = map(int, sys.stdin.readline().split())

        graph[s].append([e, w])

    start, end = map(int, sys.stdin.readline().split())

    # computing
    dijkstra(start)

    # print
    print(cost[end])