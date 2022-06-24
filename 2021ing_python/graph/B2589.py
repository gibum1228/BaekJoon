import sys
from collections import deque

IN = sys.stdin.readline

def bfs(h, w):
    que = deque([(h, w)])
    check = 0

    while que:
        y, x = que.popleft()

        for dy, dx in move:
            f_y = y + dy
            f_x = x + dx

            if 0 <= f_y < H and 0 <= f_x < W and board[f_y][f_x] != "W" and not visited[f_y][f_x]:
                visited[f_y][f_x] = True
                board[f_y][f_x] = board[y][x] + 1
                que.append((f_y, f_x))
                check = max(check, board[f_y][f_x])

    return check

if __name__ == "__main__":
    H, W = map(int, IN().split())
    board, count = [], []
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    result = 0

    for _ in range(H):
        board.append(list(IN().rstrip()))

    for h in range(H):
        for w in range(W):
            if board[h][w] != "W":
                visited = [[False for _ in range(W)] for _ in range(H)]
                board[h][w] = 0
                visited[h][w] = True
                result = max(result, bfs(h, w))

    print(result)