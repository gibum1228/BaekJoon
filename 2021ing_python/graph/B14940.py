import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    n, m = map(int, IN().split())
    G = []
    results = [[-1 for _ in range(m)] for _ in range(n)]
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    zero_position = deque([])
    goal_r, goal_c = -1, -1

    for r in range(n):
        arr = list(map(int, IN().rstrip().split()))

        for c in range(m):
            if arr[c] == 2 and goal_r == -1:
                goal_r, goal_c = r, c
            if arr[c] == 0:
                zero_position.append((r, c))

        G.append(arr)

    def bfs(r, c):
        global results
        que = deque([(r, c)])

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                dr, dc = r + mr, c + mc

                if 0 <= dr < n and 0 <= dc < m and results[dr][dc] == -1 and G[dr][dc] == 1:
                    results[dr][dc] = results[r][c] + 1
                    que.append((dr, dc))

    results[goal_r][goal_c] = 0
    bfs(goal_r, goal_c)

    for r, c in zero_position:
        results[r][c] = 0

    for result in results:
        print(*result)