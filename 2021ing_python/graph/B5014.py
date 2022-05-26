import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    F, S, G, U, D = map(int, IN().split())
    floor = [0 for _ in range(F + 1)]
    floor[S] = 1
    q = deque([S])
    while q:
        focus_floor = q.popleft()
        up, down = focus_floor + U, focus_floor - D

        if 1 <= up <= F and not floor[up]:
            floor[up] = floor[focus_floor] + 1
            q.append(up)
        if 1 <= down <= F and not floor[down]:
            floor[down] = floor[focus_floor] + 1
            q.append(down)

    print(floor[G] - 1) if floor[G] else print("use the stairs")