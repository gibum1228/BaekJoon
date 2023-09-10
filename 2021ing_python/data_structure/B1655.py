import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    left_heap, right_heap = [], []

    for _ in range(int(IN())):
        num = int(IN())

        if len(left_heap) == len(right_heap):
            heapq.heappush(left_heap, -num) # 최대힙
        else:
            heapq.heappush(right_heap, num) # 최소힙

        if right_heap and right_heap[0] < -left_heap[0]:
            left_value = -heapq.heappop(left_heap)
            right_value = heapq.heappop(right_heap)

            heapq.heappush(left_heap, -right_value)
            heapq.heappush(right_heap, left_value)

        print(-left_heap[0])