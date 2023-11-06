import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    result = 0

    # input library
    library = set()
    for _ in range(N):
        library.add(IN().rstrip())
    for _ in range(M):
        if IN().rstrip() in library:
            result += 1

    print(result)