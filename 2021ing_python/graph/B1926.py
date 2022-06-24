import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    row, col = map(int, IN().split())
    board = [list(map(int, IN().rstrip().split())) for _ in range(row)]
    picture_count, max_area = 0, 0
    visited = [[False for _ in range(col)] for _ in range(row)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(r, c):
        que = deque([(r, c)])
        count = 1

        while que:
            r, c = que.popleft()

            for mr, mc in move:
                fr, fc = r + mr, c + mc

                if 0 <= fr < row and 0 <= fc < col and board[fr][fc] == 1 and not visited[fr][fc]:
                    visited[fr][fc] = True
                    count += 1
                    que.append((fr, fc))

        return count

    for r in range(row):
        for c in range(col):
            if board[r][c] == 1 and not visited[r][c]:
                visited[r][c] = True
                picture_count += 1
                max_area = max(max_area, bfs(r, c))

    print(picture_count)
    print(max_area)