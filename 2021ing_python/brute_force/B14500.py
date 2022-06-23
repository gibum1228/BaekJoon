import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    board = [list(map(int, IN().rstrip().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    max_value = max(map(max, board))
    result = 0

    def dfs(row, col, count, sum):
        global result

        if result >= sum + (max_value * (3 - count)):
            return

        if count == 3:
            result = max(result, sum)
        else:
            for mr, mc in move:
                dr = row + mr
                dc = col + mc

                if 0 <= dr < N and 0 <= dc < M and not visited[dr][dc]:
                    if count == 1:
                        visited[dr][dc] = True
                        dfs(row, col, count + 1, sum + board[dr][dc])
                        visited[dr][dc] = False
                    visited[dr][dc] = True
                    dfs(dr, dc, count + 1, sum + board[dr][dc])
                    visited[dr][dc] = False

    for row in range(N):
        for col in range(M):
            visited[row][col] = True
            dfs(row, col, 0, board[row][col])
            visited[row][col] = False

    print(result)