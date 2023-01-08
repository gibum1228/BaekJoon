import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        N, K = map(int, IN().split()) # 건물 개수 N, 건물 규칙 개수 K
        use_time = [0] + list(map(int, IN().rstrip().split())) # 건물당 건설에 걸리는 시간
        G = {n:set() for n in range(1, N+1)}
        inDegree = [0 for _ in range(N+1)] # 진입차수
        dp = [0 for _ in range(N+1)] # 해당 건물까지 걸리는 시간

        for __ in range(K): # 건물 건설 순서
            X, Y = map(int, IN().split())
            G[X].add(Y)
            inDegree[Y] += 1
        W = int(IN())

        # 진입차수 0인 노드 넣기
        que = deque()
        for  i in range(1, N+1):
            if inDegree[i] == 0:
                que.append(i)
                dp[i] = use_time[i]

        while que:
            now_node = que.popleft()

            for next_node in G[now_node]:
                inDegree[next_node] -= 1
                if inDegree[next_node] == 0:
                    que.append(next_node)

                dp[next_node] = max(dp[next_node], dp[now_node] + use_time[next_node])

        print(dp[W])