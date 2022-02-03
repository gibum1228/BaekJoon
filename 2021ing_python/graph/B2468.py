import sys
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    board = [list(map(int, IN().split())) for _ in range(N)]
    results = [-1]
    original_visited = [[False for _ in range(N)] for _ in range(N)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    def bfs(i, j):
        que = [(i, j)]
        visited[i][j] = True

        while que:
            x, y = que.pop(0)

            for mx, my in move:
                dx = x + mx
                dy = y + my

                if 0 <= dx < N and 0 <= dy < N:
                    if board[dx][dy] > n and not visited[dx][dy]:
                        visited[dx][dy] = True
                        que.append((dx, dy))

    for n in range(1, max(max(board)) + 1):
        visited = copy.deepcopy(original_visited)
        count = 0

        for i in range(N):
            for j in range(N):
                if board[i][j] > n and not visited[i][j]:
                    count += 1
                    bfs(i, j)

        results.append(count)

    print(max(results))