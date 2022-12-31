import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    board = [list(IN().rstrip()) for _ in range(N)]
    visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌

    def bfs():
        que = deque([(0, 0, 0)]) # (row, col, is_crash)
        visited[0][0][0] = 1

        while que:
            r, c, is_crash = que.popleft()

            # 마지막 칸일 경우
            if r == N - 1 and c == M - 1:
                return visited[r][c][is_crash]

            for mr, mc in move:
                next_r = r + mr
                next_c = c + mc

                # 맵 범위에 있고 방문한 적이 없으며
                if 0 <= next_r < N and 0 <= next_c < M:
                    # 벽 안 부시고 이동
                    if board[next_r][next_c] == '0' and visited[next_r][next_c][is_crash] == 0:
                        que.append((next_r, next_c, is_crash))
                        visited[next_r][next_c][is_crash] = visited[r][c][is_crash] + 1

                    # 벽 부시고 이동
                    if board[next_r][next_c] == '1' and is_crash == 0:
                        que.append((next_r, next_c, is_crash + 1))
                        visited[next_r][next_c][is_crash + 1] = visited[r][c][is_crash] + 1

        return -1

    print(bfs())