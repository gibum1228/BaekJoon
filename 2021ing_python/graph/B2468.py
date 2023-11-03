import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    board = [list(map(int, IN().split())) for _ in range(N)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    results = 1
    many_height = 1
    ### find max height
    max_height = 0
    for row in board:
        max_height = max(max_height, sum(row))
    ### 브루트포스 알고리즘
    for height in range(2, max_height):
        visited = [[False for _ in range(N)] for _ in range(N)]
        count = 0

        for r in range(N):
            for c in range(N):
                if board[r][c] >= height and not visited[r][c]:
                    count += 1
                    visited[r][c] = True
                    que = deque([(r, c)])
                    ## bfs
                    while que:
                        now_r, now_c = que.popleft()

                        for mr, mc in move:
                            next_r, next_c = now_r + mr, now_c + mc

                            if 0 <= next_r < N and 0 <= next_c < N \
                                and not visited[next_r][next_c] \
                                and board[next_r][next_c] >= height:
                                visited[next_r][next_c] = True
                                que.append((next_r, next_c))

        if count > results:
            results = count
            many_height = height
    ### print
    print(results)