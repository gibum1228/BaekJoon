import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    visited = [False for _ in range(100001)] # -1 기능이 있기 때문에 K-1까지는 노드 정보가 있어야 함
    visited[N] = True
    que = deque([(N, 0)]) # (node, time)

    if N == K:
        print(0)
        que = []

    while que:
        node, time = que.popleft()

        for next_node, next_time in [(node*2, 0), (node+1, 1), (node-1, 1)]:
            if next_node >= len(visited) or next_node < 0:
                continue

            if next_node == K:
                print(time + next_time)
                que = []
                break

            if next_time == 1 and not visited[next_node]: # 0-1 BFS
                que.append((next_node, time + next_time))
            elif next_time == 0 and not visited[next_node]:
                que.appendleft((next_node, time + next_time))

            visited[next_node] = True