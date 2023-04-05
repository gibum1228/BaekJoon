import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    result = 0
    values = []

    for _ in range(N):
        values.append(int(IN()))

    values.sort(reverse=True)

    for value in values:
        count = K // value

        if count != 0:
            K -= value * count
            result += count

    print(result)