import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    N_position = {}
    M_position = {}

    # input
    for _ in range(N):
        k, v = map(int, IN().split())

        N_position[k] = v
    for _ in range(M):
        k, v = map(int, IN().split())

        M_position[k] = v

    # bfs
    def bfs():
        que = deque([(1, 0)])
        visited = [False for _ in range(101)]
        visited[1] = True

        while que:
            now_num, now_cost = que.popleft()

            # 주사위 굴리기
            for x in range(1, 7):
                next_num = now_num + x

                if next_num == 100:
                    return now_cost + 1
                elif next_num < 100 and not visited[next_num]:
                    N_trigger = N_position.get(next_num, -1)
                    M_trigger = M_position.get(next_num, -1)

                    if N_trigger != -1:
                        next_num = N_trigger
                    elif M_trigger != -1:
                        next_num = M_trigger

                    if not visited[next_num]:
                        visited[next_num] = True
                        que.append((next_num, now_cost + 1))

    print(bfs())