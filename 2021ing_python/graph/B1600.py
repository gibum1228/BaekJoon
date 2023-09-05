import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    K = int(IN())
    C, R = map(int, IN().split())
    G = [list(map(int, IN().split())) for _ in range(R)]
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    horse_move = [(-1, -2), (-2, -1), (-1, 2), (-2, 1),
                  (1, -2), (2, -1), (1, 2), (2, 1)]

    def bfs():
        visited = [[[0 for _ in range(K+1)] for _ in range(C)] for _ in range(R)]
        que = deque([(0, 0, 0)])
        visited[0][0][0] = 1

        while que:
            r, c, horse_count = que.popleft()

            # 인접한 4 방향
            for mr, mc in move:
                next_r, next_c = r + mr, c + mc

                if next_r == R-1 and next_c == C-1:
                    return visited[r][c][horse_count]

                if 0 <= next_r < R and 0 <= next_c < C and not visited[next_r][next_c][horse_count] and not G[next_r][next_c]:
                    visited[next_r][next_c][horse_count] = visited[r][c][horse_count] + 1
                    que.append((next_r, next_c, horse_count))
            if horse_count < K:
                # 말 행동 따라하기
                for mr, mc in horse_move:
                    next_r, next_c = r + mr, c + mc

                    if next_r == R - 1 and next_c == C - 1:
                        return visited[r][c][horse_count]

                    if 0 <= next_r < R and 0 <= next_c < C and not visited[next_r][next_c][horse_count + 1] and not G[next_r][next_c]:
                        visited[next_r][next_c][horse_count + 1] = visited[r][c][horse_count] + 1
                        que.append((next_r, next_c, horse_count + 1))

        return -1


    if R == 1 and C == 1:
        print(0)
    else:
        print(bfs())