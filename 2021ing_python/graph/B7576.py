import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    M, N = map(int, IN().split())
    G = []
    position = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for y in range(N):
        arr = list(map(int, IN().rstrip().split()))
        G.append(arr)

        for x in range(len(arr)):
            if arr[x] == 1:
                position.append((y, x))
                visited[y][x] = True

    def bfs():
        global position

        while position:
            y, x = position.popleft()

            for my, mx in move:
                dx, dy = mx + x, my + y

                if 0 <= dx < M and 0 <= dy < N:
                    if G[dy][dx] == 0 and not visited[dy][dx]:
                        G[dy][dx] = G[y][x] + 1
                        position.append((dy, dx))
                        visited[dy][dx] = True

    bfs()

    day = -1
    for i in G:
        if 0 in i:
            day = -1
            break
        day = max(day, max(i) - 1)

    print(day)