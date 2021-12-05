import sys

input = sys.stdin.readline

def back_tracking():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(1, N+1):
        if i not in s:
            s.append(i)
            back_tracking()
            s.pop()

if __name__ == "__main__":
    N, M = map(int, input().split())
    s = []

    back_tracking()