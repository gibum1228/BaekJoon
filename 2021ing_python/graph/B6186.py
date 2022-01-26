import sys

input = sys.stdin.readline

def bfs(i, j):
    que = [(i, j)]

    while que:
        x, y = que.pop(0)
        visited[x][y] = True

        for dx, dy in move:
            dx += x
            dy += y

            if 0 <= dx < R and 0 <= dy < C:
                if not visited[dx][dy] and board[dx][dy] == '#':
                    que.append((dx, dy))

if __name__ == "__main__":
    count = 0
    R, C = map(int, input().split())
    board = [list(input().rstrip()) for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for i in range(R):
        for j in range(C):
            if board[i][j] == '#' and not visited[i][j]:
                count += 1
                bfs(i, j)

    print(count)