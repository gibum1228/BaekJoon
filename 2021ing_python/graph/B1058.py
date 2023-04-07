import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    G = [list(IN().rstrip()) for _ in range(N)]
    friend_count = [[0] * N for _ in range(N)]

    for other in range(N):
        for me in range(N):
            for friend in range(N):
                if me == friend: continue

                if G[me][friend] == 'Y' or (G[me][other] == 'Y' and G[other][friend] == 'Y'):
                    friend_count[me][friend] = 1

    result = 0
    for FC in friend_count:
        result = max(result, sum(FC))

    print(result)