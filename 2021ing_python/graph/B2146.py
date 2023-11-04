import sys
from collections import deque
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    G = [list(map(int, IN().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    positions = dict()

    # BFS
    def bfs(start_r, start_c, label):
        que = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        G[start_r][start_c] = label
        positions[label] = set()

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                next_r, next_c = r + mr, c + mc

                if 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c]:
                    if G[next_r][next_c] == 1:
                        visited[next_r][next_c] = True
                        que.append((next_r, next_c))
                        G[next_r][next_c] = label
                    else:
                        positions[label].add((r, c, 0))

    # BFS으로 영역 구분
    label = 1
    for r in range(N):
        for c in range(N):
            if not visited[r][c] and G[r][c] == 1:
                bfs(r, c, label)
                label += 1

    # label별 거리 비교
    def bfs2(position, label, results):
        que = deque(position)
        copy_visited = copy.deepcopy(visited)

        while que:
            r, c, count = que.popleft()

            for mr, mc in move:
                next_r, next_c = r + mr, c + mc

                if 0 <= next_r < N and 0 <= next_c < N:
                    if G[next_r][next_c] > 0 and G[next_r][next_c] != label:
                        return count

                    if not copy_visited[next_r][next_c]:
                        copy_visited[next_r][next_c] = True
                        if count + 1 < results:
                            que.append((next_r, next_c, count + 1))

        return float('inf')

    # label별 bfs 실행
    results = float('inf')
    for label in positions.keys():
        results = min(results, bfs2(positions[label], label, results))
    print(results)