import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        V, E = map(int, IN().split())
        visited = [0 for _ in range(V+1)] # 0: 기초, 1 or 2로 이분 그래프 구분
        G = {k: set() for k in range(1, V+1)}
        trigger = True

        for _ in range(E):
            u, v = map(int, IN().split())

            G[u].add(v)
            G[v].add(u)

        def bfs(start_node):
            que = deque([(start_node, 1)])
            visited[start_node] = 1

            while que:
                now_node, now_num = que.popleft()

                for next_node in G[now_node]:
                    if visited[next_node] == now_num:
                        return False
                    elif visited[next_node] == 0:
                        next_num = 2 if now_num == 1 else 1
                        visited[next_node] = next_num
                        que.append((next_node, next_num))

            return True

        for i in range(1, V+1):
            if visited[i] == 0:
                trigger = bfs(i)

                if not trigger:
                    break

        print("YES" if trigger else "NO")