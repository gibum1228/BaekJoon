import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    mod = 1000000000
    table = [1]
    table += [0] * N

    for _ in range(1, K + 1):
        for idx in range(1, N + 1):
            table[idx] = (table[idx] + table[idx - 1]) % mod

    print(str(table[N]))