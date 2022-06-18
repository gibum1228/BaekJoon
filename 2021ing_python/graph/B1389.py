import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    G = [[] for _ in range(N+1)]
    result = []

    for _ in range(M):
        A, B = map(int, IN().split())

        G[A].append(B)
        G[B].append(A)

    def bfs(start):
        distance = [1 if x in G[start] else 0 for x in range(N+1)]
        que = deque([(x, 1) for x in G[start]])

        while que:
            focus_x, dist = que.popleft()

            for next_x in G[focus_x]:
                if distance[next_x] == 0 and next_x != start:
                    distance[next_x] = dist + 1
                    que.append((next_x, dist + 1))

        return sum(distance)

    min_index, min_num = -1, float('inf')
    for i in range(1, N+1):
        num = bfs(i)
        result.append(num)
        if num < min_num:
            min_index, min_num = i, num

    print(min_index)