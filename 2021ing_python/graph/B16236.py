import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    G = []
    for r in range(N):
        row = list(map(int, IN().split()))
        G.append(row)

        for c, x in enumerate(row):
            if x == 9:
                start_r, start_c = r, c
    G[start_r][start_c] = 0

    def bfs(r, c):
        que = deque([(r, c)])
        visited = [[0 for _ in range(N)] for _ in range(N)]
        visited[r][c] = 1
        candi = []

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                next_r, next_c = r + mr, c + mc

                if 0 <= next_r < N and 0 <= next_c < N and visited[next_r][next_c] == 0 and G[next_r][next_c] <= size:
                    if 0 < G[next_r][next_c] < size:
                        candi.append((visited[r][c], next_r, next_c))

                    visited[next_r][next_c] = visited[r][c] + 1
                    que.append((next_r, next_c))

        if candi:
            candi.sort()
        else:
            candi = [(0, -1, -1)]

        return candi[0]

    size = 2
    eat = 0
    sec = 0
    while True:
        need_sec, next_r, next_c = bfs(start_r, start_c)

        if next_r == -1 and next_c == -1:
            print(sec)
            break
        else:
            eat += 1
            if size == eat:
                size += 1
                eat = 0
            G[next_r][next_c] = 0
            sec += need_sec
            start_r, start_c = next_r, next_c