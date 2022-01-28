import sys

input = sys.stdin.readline

def bfs(i, j):
    que = [(i, j)]
    visited[i][j] = True

    while que:
        x, y = que.pop(0)

        for dx, dy in move:
            dx += x
            dy += y

            if 0 <= dx < h and 0 <= dy < w:
                if not visited[dx][dy] and board[dx][dy] == 1:
                    visited[dx][dy] = True
                    que.append((dx, dy))

if __name__ == "__main__":
    move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]

    while True:
        w, h = map(int, input().split())

        # exit
        if w == 0 and h == 0:
            break

        count = 0
        board = [[] for _ in range(h)]
        visited = [[False for _ in range(w)] for _ in range(h)]

        for i in range(h):
            board[i] = list(map(int, input().rstrip().split()))

        for i in range(h):
            for j in range(w):
                if board[i][j] == 1 and not visited[i][j]:
                    count += 1
                    bfs(i, j)

        print(count)