import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())

    results = []
    G = [[] for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    que = []

    # 그래프 생성
    for _ in range(M):
        start, end = map(int, IN().split())

        G[start].append(end)
        degree[end] += 1

    # 진입차수 0인 노드 저장
    for i in range(1, N+1):
        if degree[i] == 0:
            que.append(i)

    # 위상 정렬
    while que:
        now_node = heapq.heappop(que)
        results.append(now_node)

        for next_node in G[now_node]:
            degree[next_node] -= 1

            if degree[next_node] == 0:
                heapq.heappush(que, next_node)

    # print
    print(*results)