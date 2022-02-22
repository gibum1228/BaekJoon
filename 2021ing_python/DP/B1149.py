import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    dp = []

    for i in range(N):
        dp.append([[], [], []])
        R, G, B = map(int, IN().split())

        if i == 0:
            dp[0] = [(R, "r"), (G, "g"), (B, "b")]
        else:
            for j in range(3):
                if dp[i - 1][j][1] == "r":
                    if G < B:
                        dp[i][j] = (dp[i - 1][j][0] + G, "g")
                    else:
                        dp[i][j] = (dp[i - 1][j][0] + B, "b")
                elif dp[i - 1][j][1] == "g":
                    if R < B:
                        dp[i][j] = (dp[i - 1][j][0] + R, "r")
                    else:
                        dp[i][j] = (dp[i - 1][j][0] + B, "b")
                else:
                    if R < G:
                        dp[i][j] = (dp[i - 1][j][0] + R, "r")
                    else:
                        dp[i][j] = (dp[i - 1][j][0] + G, "g")

    print(min(dp[-1])[0])