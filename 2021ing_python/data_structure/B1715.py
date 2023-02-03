import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    que = []
    dp = []

    for _ in range(int(IN())):
        heapq.heappush(que, int(IN()))

    while que:
        if len(que) == 1: break
        a = heapq.heappop(que)
        b = heapq.heappop(que)

        heapq.heappush(que, a + b)
        dp.append(a+b)

    print(sum(dp))