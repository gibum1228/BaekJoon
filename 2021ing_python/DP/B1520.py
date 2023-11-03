import sys
sys.setrecursionlimit(10 ** 8)

IN = sys.stdin.readline

if __name__ == "__main__":
    R, C = map(int, IN().split())
    board = [list(map(int, IN().split())) for _ in range(R)]
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    dp = [[-1 for _ in range(C)] for _ in range(R)]

    def dfs(r, c):
        if r == R-1 and c == C-1:
            return 1

        if dp[r][c] != -1:
            return dp[r][c]

        count = 0
        for mr, mc in move:
            next_r, next_c = r + mr, c + mc

            if 0 <= next_r < R and 0 <= next_c < C and board[r][c] > board[next_r][next_c]:
                count += dfs(next_r, next_c)

        dp[r][c] = count

        return dp[r][c]

    print(dfs(0, 0))