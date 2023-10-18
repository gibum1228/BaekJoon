import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M, K = map(int, IN().split())
    # init graph and wall position
    board = [list(IN().rstrip()) for _ in range(N)]

    # bfs
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    que = deque([(0, 0, 0)]) # (r, c, k)
    visited_positions = [[[0 for _ in range(K+1)] for _ in range(M)] for _ in range(N)] # (N, M, K)
    visited_positions[0][0][0] = 1

    if N == 1 and M == 1:
        print(1)
    else:
        while que:
            r, c, k = que.popleft()

            for mr, mc in move:
                next_r, next_c = r + mr, c + mc
                if next_r == N-1 and next_c == M-1:
                    print(visited_positions[r][c][k] + 1)
                    exit()

                if 0 <= next_r < N and 0 <= next_c < M and (next_r, next_c):
                    # 그냥 이동
                    if board[next_r][next_c] == '0' and visited_positions[next_r][next_c][k] == 0:
                        visited_positions[next_r][next_c][k] = visited_positions[r][c][k] + 1
                        que.append((next_r, next_c, k))

                    # 벽 부시고 이동
                    if k < K and board[next_r][next_c] == '1' and visited_positions[next_r][next_c][k+1] == 0:
                        visited_positions[next_r][next_c][k+1] = visited_positions[r][c][k] + 1
                        que.append((next_r, next_c, k+1))

        print(-1)