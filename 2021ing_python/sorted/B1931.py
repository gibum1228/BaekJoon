import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    info = []

    for _ in range(N):
        info.append(tuple(map(int, IN().rstrip().split())))

    info.sort(key=lambda x: (x[1], x[0]))

    count = 1
    end = info[0][1]
    for i in range(1, N):
        if info[i][0] >= end:
            count += 1
            end = info[i][1]

    print(count)