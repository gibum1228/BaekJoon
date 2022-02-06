import sys

IN = sys.stdin.readline

def bfs(i, j):
    que = [(i, j)]
    visited[i][j] = True
    count = 1

    while que:
        x, y = que.pop(0)

        for mx, my in move:
            dx = x + mx
            dy = y + my

            if 0 <= dx < N and 0 <= dy < M:
                if not board[dx][dy] and not visited[dx][dy]:
                    que.append((dx, dy))
                    visited[dx][dy] = True
                    count += 1

    results.append(count)

if __name__ == "__main__":
    results = []
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    M, N, K = map(int, IN().split())
    board = [[False for j in range(M)] for i in range(N)]
    visited = [[False for j in range(M)] for i in range(N)]

    for _ in range(K):
        x1, y1, x2, y2 = map(int, IN().split())

        for x in range(x1, x2):
            for y in range(y1, y2):
                board[x][y] = True
                visited[x][y] = True

    for i in range(N):
        for j in range(M):
            if not board[i][j] and not visited[i][j]:
                bfs(i, j)

    print(len(results))
    print(" ".join(map(str, sorted(results))))