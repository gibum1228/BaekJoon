import sys
from collections import deque
from itertools import combinations
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    virus_position = []
    visited = [[0 for _ in range(N)] for _ in range(N)]
    G = []
    for r in range(N):
        row = list(map(int, IN().split()))
        G.append(row)

        for c, x in enumerate(row):
            if x == 1: # 벽
                visited[r][c] = -1
            if x == 2: # 바이러스 지정 가능 위치
                virus_position.append((r, c))

    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    combi = list(combinations(virus_position, M))

    def bfs(combi_x, visited):
        que = deque([])
        for (r, c) in combi_x:
            visited[r][c] = 1
            que.append((r, c))
        result = 0

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                next_r, next_c = r + mr, c + mc

                if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                    visited[next_r][next_c] = visited[r][c] + 1
                    que.append((next_r, next_c))

        # 최대 소요 시간 찾기 및 불가능
        for row in visited:
            if row.count(0) > 0:
                return 99999999

            result = max(result, max(row))
        return result - 1

    # logic
    results = []
    for combi_x in combi:
        results.append(bfs(combi_x, copy.deepcopy(visited)))

    result = min(results)
    print(result if result != 99999999 else -1)