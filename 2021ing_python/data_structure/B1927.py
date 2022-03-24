import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arr = []
    results = ""

    for _ in range(N):
        order = int(IN())

        if order == 0:
            if arr:
                results += f"{heapq.heappop(arr)}\n"
            else:
                results += f"{0}\n"
        else:
            heapq.heappush(arr, order)
    
    print(results)