import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    M, N = map(int, IN().split())
    board = [list(IN().rstrip()) for _ in range(N)]
    result_w, result_b = 0, 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    def bfs(r, c):
        word = board[r][c]
        count = 1
        que = deque([(r, c)])

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                dr, dc = r + mr, c + mc

                if 0 <= dr < N and 0 <= dc < M and not visited[dr][dc] and board[dr][dc] == word:
                    que.append((dr, dc))
                    visited[dr][dc] = True
                    count += 1

        return (0, count**2) if word == "B" else (count**2, 0)

    for r in range(N):
        for c in range(M):
            if not visited[r][c]:
                visited[r][c] = True
                count_w, count_b = bfs(r, c)
                result_w += count_w
                result_b += count_b

    print(result_w, result_b)