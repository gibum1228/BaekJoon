import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    jewelry = []
    N, K = map(int, IN().split()) # 보석 개수, 가방 개수

    for _ in range(N): # 보석 정보
        M, V = map(int, IN().split()) # 무게, 가격
        heapq.heappush(jewelry, (M, V))

    bag = [] # 가방별 무게 정보
    for _ in range(K):
        C = int(IN())
        heapq.heappush(bag, C)

    result = 0
    DB = [] # 해당 가방에 들어갈 수 있는 보석의 무게 정보
    while bag:
        now_bag = heapq.heappop(bag) # 현재 가방 무게

        while jewelry: # 현재 가방 무게에 들어가는 보석 무게를 모두 DB에 넣기
            now_M, now_V = heapq.heappop(jewelry)

            if now_M <= now_bag: # 현재 가방에 보석을 넣을 수 있으면
                heapq.heappush(DB, -now_V)
            else:
                heapq.heappush(jewelry, (now_M, now_V)) # 보석 정보 원상복구
                break

        result += -heapq.heappop(DB) if DB else 0

    print(result)