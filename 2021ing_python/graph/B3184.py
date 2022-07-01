import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, IN().split())
    board = [list(IN().rstrip()) for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    o_alive, v_alive = 0, 0

    def what(c):
        if c == 'o': return 1, 0
        elif c == 'v': return 0, 1
        else: return 0, 0

    def bfs(r, c):
        que = deque([(r, c)])
        o_count, v_count = what(board[r][c])

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                dr, dc = r + mr, c + mc

                if 0 <= dr <  R and 0 <= dc < C and board[dr][dc] != '#' and not visited[dr][dc]:
                    que.append((dr, dc))
                    visited[dr][dc] = True
                    if board[dr][dc] == 'o': o_count += 1
                    elif board[dr][dc] == 'v': v_count += 1

        if o_count > v_count:
            return o_count, 0
        else:
            return 0, v_count

    for r in range(R):
        for c in range(C):
            if board[r][c] != '#' and not visited[r][c]:
                visited[r][c] = True
                o, v = bfs(r, c)
                o_alive += o
                v_alive += v

    print(f"{o_alive} {v_alive}")