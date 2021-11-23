import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    note = dict()
    results = ""

    for _ in range(N):
        site, pwd = input().rstrip().split()

        note[site] = pwd

    for _ in range(M):
        site = input().rstrip()

        results += note[site] + "\n"

    print(results)