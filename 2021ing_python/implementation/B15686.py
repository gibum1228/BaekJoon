import sys
from itertools import combinations

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    board, city, chicken = [], [], []
    result = float('inf')

    for i in range(N):
        board.append(list(map(int, IN().rstrip().split())))
        for j in range(N):
            if board[i][j] == 1:
                city.append((i, j))
            if board[i][j] == 2:
                chicken.append((i, j))

    for k in combinations(chicken, M):
        tmp = 0
        for c in city:
            distance = float('inf')

            for i in range(M):
                distance = min(distance, abs(c[0] - k[i][0]) + abs(c[1] - k[i][1]))
            tmp += distance
        result = min(result, tmp)

    print(result)