import sys

input = sys.stdin.readline


def back_tracking(back_num):
    if len(s) == M:
        try:
            if locker.index(s):
                pass
        except:
            print(' '.join(map(str, s)))
            locker.append(s.copy())

        return

    for i in arr:
        if i >= back_num:
            s.append(i)
            back_tracking(i)
            s.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().rstrip().split())))
    s = []
    locker = []

    back_tracking(0)