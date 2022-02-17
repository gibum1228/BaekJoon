import copy
import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    H, W = map(int, IN().split())
    board = [list(IN().rstrip()) for _ in range(H)]
    move = [(-1, 0), (0, 1), (1, 0), (-1, 0)]
    results = []

    def bfs(x, y):
        que = [(x, y)]
        next_que = []
        visited[x][y] = True
        count = 0

        while que:
            count += 1

            for x, y in que:
                for mx, my in move:
                    dx = x + mx
                    dy = y + my

                    if 0 <= dx < H and 0 <= dy < W:
                        if board[dx][dy] == 'L' and not visited[dx][dy]:
                            next_que.append((dx, dy))
                            visited[dx][dy] = True

            que = copy.deepcopy(next_que)
            next_que = []

        return count

    for x in range(H):
        for y in range(W):
            if board[x][y] == 'L':
                visited = [[False for _ in range(W)] for _ in range(H)]
                results.append(bfs(x, y))

    print(max(results))