import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    n, w, L = map(int, IN().split())
    arr = deque(list(map(int, IN().split())))
    on_bridge = deque([])

    sec = 0
    bridge_weight = 0
    while arr or on_bridge:
        sec += 1

        if on_bridge and sec == on_bridge[0][1] + w :  # 다리 탈출
            bridge_weight -= on_bridge.popleft()[0]

        if arr and bridge_weight + arr[0] <= L: # 다리 위에 트럭 올라가기
            bridge_weight += arr[0]
            on_bridge.append((arr.popleft(), sec))

    print(sec)