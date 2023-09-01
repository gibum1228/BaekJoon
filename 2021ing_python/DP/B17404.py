import sys
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    color = []

    for _ in range(N):
        color.append(list(map(int, IN().split())))

    color1 = copy.deepcopy(color)
    color2 = copy.deepcopy(color)
    color3 = copy.deepcopy(color)

    # 1~2 번째
    color1[1][1] += color1[0][0]
    color1[1][2] += color1[0][0]
    color2[1][0] += color2[0][1]
    color2[1][2] += color2[0][1]
    color3[1][0] += color3[0][2]
    color3[1][1] += color3[0][2]

    if N >= 3:
        # 3 번째
        color1[2][0] += min(color1[1][1], color1[1][2])
        color1[2][1] += color1[1][2]
        color1[2][2] += color1[1][1]
        color2[2][0] += color2[1][2]
        color2[2][1] += min(color2[1][0], color2[1][2])
        color2[2][2] += color2[1][0]
        color3[2][0] += color3[1][1]
        color3[2][1] += color3[1][0]
        color3[2][2] += min(color3[1][0], color3[1][1])

        if N > 3:
            # 그 사이
            for i in range(3, N):
                for color in [color1, color2, color3]:
                    color[i][0] += min(color[i - 1][1], color[i - 1][2])
                    color[i][1] += min(color[i - 1][0], color[i - 1][2])
                    color[i][2] += min(color[i - 1][0], color[i - 1][1])

    print(min(color1[-1][1], color1[-1][2], color2[-1][0], color2[-1][2], color3[-1][0], color3[-1][1]))