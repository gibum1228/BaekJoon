import sys

def bfs(board, x, y):
    que = [(x, y)]

    while que:
        focus_x, focus_y = que.pop(0)
        visited[focus_x][focus_y] = True

        for dx, dy in move:
            dx += focus_x
            dy += focus_y

            if 0 <= dx < M and 0 <= dy < N:
                if board[dx][dy] == 1 and not visited[dx][dy]:
                    que.append((dx, dy))
                    position.remove((dx, dy))

if __name__ == "__main__":
    T = int(sys.stdin.readline())
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    for _ in range(T):
        count = 0
        M, N, K = map(int, sys.stdin.readline().split())
        board = [[0 for _ in range(N)] for _ in range(M)]
        visited = [[False for _ in range(N)] for _ in range(M)]
        position = []

        for _ in range(K):
            X, Y = map(int, sys.stdin.readline().split())
            board[X][Y] = 1
            position.append((X, Y))
            
        for x, y in position:
            if not visited[x][y]:
                count += 1
                bfs(board, x, y)

        print(count)