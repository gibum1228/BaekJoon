import sys

input = sys.stdin.readline


def back_tracking():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    back_num = 0
    for i in range(0, N):
        if not visited[i] and back_num != arr[i]:
            visited[i] = True
            s.append(arr[i])
            back_num = arr[i]
            back_tracking()
            visited[i] = False
            s.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().rstrip().split())))
    s = []
    visited = [False] * N

    back_tracking()