import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    visited_sick = [[False for _ in range(N)] for _ in range(N)]
    visited_not_sick = [[False for _ in range(N)] for _ in range(N)]
    board = [list(IN().rstrip()) for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    result = [0, 0]

    def bfs(key, i, j, sick):
        que = [(i, j)]
        if sick:
            visited_sick[i][j] = True
        else:
            visited_not_sick[i][j] = True

        while que:
            x, y = que.pop(0)

            for dx, dy in move:
                xx, yy = x + dx, y + dy

                if 0 <= xx < N and 0 <= yy < N:
                    if sick:
                        if key == 'R' or key == 'G':
                            if board[xx][yy] == 'B':
                                continue
                        else:
                            if not board[xx][yy] == key:
                                continue

                        if not visited_sick[xx][yy]:
                            visited_sick[xx][yy] = True
                            que.append((xx, yy))
                    else:
                        if not visited_not_sick[xx][yy] and board[xx][yy] == key:
                            visited_not_sick[xx][yy] = True
                            que.append((xx, yy))

    for i in range(N):
        for j in range(N):
            if not visited_sick[i][j]:
                result[1] += 1
                bfs(board[i][j], i, j, True)
            if not visited_not_sick[i][j]:
                result[0] += 1
                bfs(board[i][j], i, j, False)

    print(" ".join(map(str, result)))