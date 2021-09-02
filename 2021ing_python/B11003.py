import sys
from collections import deque


if __name__ == "__main__":
    N, L = map(int, sys.stdin.readline().split())
    A = list(map(int, sys.stdin.readline().rstrip().split()))
    dq = deque()
    D = [0 for _ in range(N)]

    for i in range(N):
        while dq and dq[-1][0] > A[i]:
            dq.pop()

        while dq and dq[0][1] <= i-L:
            dq.popleft()

        dq.append((A[i], i))
        D[i] = dq[0][0]

    print(*D)