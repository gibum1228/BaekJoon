import sys

input = sys.stdin.readline

def back_tracking(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(start, N+1):
        if i not in s:
            s.append(i)
            back_tracking(i+1)
            s.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    s = []

    back_tracking(1)