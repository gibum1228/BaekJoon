import sys
from collections import deque

IN = sys.stdin.readline
INF = float('inf')

if __name__ == "__main__":
    S = int(IN())
    results = [[INF for _ in range(S+2)] for _ in range(S+2)]

    def bfs():
        queue = deque([(1, 0)])
        results[1][0] = 0

        while queue:
            screen, clip_board = queue.popleft()

            if results[screen][screen] == INF:
                queue.append((screen, screen))
                results[screen][screen] = results[screen][clip_board] + 1
            if screen + clip_board < S + 2 and results[screen + clip_board][clip_board] == INF:
                queue.append((screen + clip_board, clip_board))
                results[screen + clip_board][clip_board] = results[screen][clip_board] + 1
            if screen >= 1 and results[screen - 1][clip_board] == INF:
                queue.append((screen - 1, clip_board))
                results[screen - 1][clip_board] = results[screen][clip_board] + 1

    bfs()
    print(min(results[S]))