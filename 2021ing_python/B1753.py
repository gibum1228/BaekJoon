import heapq
import sys

def logic(K):
    que = [] # 우선순위 큐 -> (가중치, 노드)를 담고 가중치 기준으로 정렬

    heapq.heappush(que, (0, K)) # 큐에 시작노드((0, K)) 삽입
    min_path[K] = 0 # 시작점은 최단 경로 0

    while que:
        distance, focus = heapq.heappop(que) # 가중치가 가장 짧은 노드 정보 가져오기

        # 이미 최소값이 설정된 노드이면 탐색하지 않음
        if (min_path[focus] < distance) and (min_path[focus] > -1):
            continue

        # 연결된 노드(focus)를 거쳐 지나가는 최단 경로들 갱신하기
        for i in graph[focus]:
            sum = distance + i[1] # 누적 가중치

            # 현재보다 최단 경로거나 처음 호출된 것이라면 최단 거리 갱신
            if (sum < min_path[i[0]]) or (min_path[i[0]] == -1):
                min_path[i[0]] = sum
                heapq.heappush(que, (sum, i[0]))

if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    K = int(sys.stdin.readline())

    graph = [[] for _ in range(V+1)]
    min_path = [-1] * (V+1)

    # input
    for i in range(E):
        u, v, w = map(int, sys.stdin.readline().split())

        graph[u].append([v, w])

    # logic
    logic(K)

    # print
    for i in range(1, V+1):
        if min_path[i] == -1:
            print("INF")
        else:
            print(min_path[i])