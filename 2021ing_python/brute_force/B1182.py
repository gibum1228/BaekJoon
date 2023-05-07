import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, S = map(int, IN().split())
    arr = list(map(int, IN().split()))
    count = 0

    def recursion(focus, idx):
        global count

        if focus and sum(focus) == S:
            count += 1

        for i in range(idx, N):
            focus.append(arr[i])
            recursion(focus, i+1)
            focus.pop()

    recursion([], 0)

    print(count)