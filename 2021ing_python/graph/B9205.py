import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())

    for _ in range(T):
        result = "sad"
        market = int(IN())

        # input
        now_x, now_y = map(int, IN().split()) # 집 위치
        market_position = [tuple(map(int, IN().rstrip().split())) for _ in range(market)] # 편의점들 위치
        visited = [False for _ in range(market)]
        end_x, end_y = map(int, IN().split()) # 락 페스티벌 위치

        # bfs
        q = deque([(now_x, now_y)])

        while q:
            x, y = q.popleft()

            if abs(x - end_x) + abs(y - end_y) <= 1000: # 락 페스티벌에 갈 수 있음
                result = "happy"
                break

            for i in range(market):
                if not visited[i]:
                    market_x, market_y = market_position[i]
                    if abs(x - market_x) + abs(y - market_y) <= 1000: # 다음 편의점에 갈 수 있음
                        q.append((market_x, market_y))
                        visited[i] = True

        print(result)