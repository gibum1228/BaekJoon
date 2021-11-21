import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, input().split())
    book = dict()

    for i in range(1, N+1):
        name = input().rstrip()
        i = str(i)
        book[name] = i
        book[i] = name

    for _ in range(M):
        print(book[input().rstrip()])