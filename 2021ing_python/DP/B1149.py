import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    color = []

    for i in range(N):
        color.append(list(map(int, IN().split())))

    for i in range(1, N):
        color[i][0] += min(color[i - 1][1], color[i - 1][2])
        color[i][1] += min(color[i - 1][0], color[i - 1][2])
        color[i][2] += min(color[i - 1][0], color[i - 1][1])

    print(min(color[-1]))