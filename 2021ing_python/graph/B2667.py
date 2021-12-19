import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    count_arr = []
    board = [list(IN().rstrip()) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(i, j):
        que = [(i, j)]
        count = 1

        while que:
            x, y = que.pop(0)
            visited[x][y] = True

            for px, py in move:
                tx, ty = x+px, y+py

                if 0 <= tx < N and 0 <= ty < N:
                    if board[tx][ty] == '1':
                        if not visited[tx][ty] and (tx, ty) not in que:
                            que.append((tx, ty))
                            count += 1
                    else:
                        visited[tx][ty] = True

        count_arr.append(count)

    for i in range(N):
        for j in range(N):
            if board[i][j] == '1':
                if not visited[i][j]:
                    bfs(i, j)
            else:
                visited[i][j] = True

    count_arr.sort()
    print(len(count_arr))
    print("\n".join(map(str, count_arr)))