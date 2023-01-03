import sys
from collections import deque

IN = sys.stdin.readline

# 위상 정렬 함수
def topology_sort(G, start_arr, use_time, W):
    dp = [use_time[i] for i in range(len(use_time))]

    # 진입차수 0인 시작점 노드들 큐에 넣기
    que = deque(start_arr)

    # 큐가 빌 때까지 반복
    while que:
        # 큐에서 원소 꺼내기
        now_node = que.popleft()

        # 해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for next_node in G[now_node]:
            next_weight = dp[now_node] + use_time[next_node]
            dp[next_node] = max(dp[next_node], next_weight)
            que.append((next_node, next_weight))

    return dp[W]

if __name__ == "__main__":
    for _ in range(int(IN())):
        N, K = map(int, IN().split()) # 건물 개수 N, 건물 규칙 개수 K
        use_time = [0] + list(map(int, IN().rstrip().split())) # 건물당 건설에 걸리는 시간
        G = {n:set() for n in range(1, N+1)}
        in_count = [0 for __ in range(N+1)] # 진입차수
        for __ in range(K): # 건물 건설 순서
            X, Y = map(int, IN().split())
            G[X].add(Y)
            in_count[Y] += 1
        W = int(IN())

        start_arr = []
        for i, count in enumerate(in_count):
            if count == 0 and i > 0:
                start_arr.append(i)
        print(start_arr); exit()
        print(topology_sort(G, start_arr, use_time, W))