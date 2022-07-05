import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    # 양 숫자 세기
    def bfs(r, c):
        que = deque([(r, c)])

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                dr, dc = mr + r, mc + c

                if 0 <= dr < R and 0 <= dc < C and G[dr][dc] == "#" and not visited[dr][dc]:
                    que.append((dr, dc))
                    visited[dr][dc] = True

    for _ in range(T):
        R, C = map(int, IN().split())
        G = [list(IN().rstrip()) for _ in range(R)]
        visited = [[False for _ in range(C)] for _ in range(R)]
        count = 0

        for r in range(R):
            for c in range(C):
                if G[r][c] == '#' and not visited[r][c]:
                    visited[r][c] = True
                    count += 1
                    bfs(r, c)

        print(count)