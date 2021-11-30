import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    que = []

    for _ in range(N):
        num = int(input())

        if num != 0:
            heapq.heappush(que, (abs(num), num))
        else:
            if que:
                _, x = heapq.heappop(que)
                print(x)
            else:
                print(0)