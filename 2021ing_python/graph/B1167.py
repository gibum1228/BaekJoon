import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    V = int(IN())
    ### create graph
    G = {k: [] for k in range(1, V+1)}
    for _ in range(V):
        info = list(map(int, IN().split()))

        for i in range(2, len(info), 2):
            G[info[0]].append((info[i-1], info[i])) # (next_node, distance)
    # print("== 트리 정보 ==")
    # for k, v in G.items():
    #     print(k, ">>", v)
    ### bfs
    def bfs(start_node):
        global result
        que = deque([[start_node, 0]]) # (node, distance)
        visited = [False for _ in range(V+1)]
        visited[start_node] = True
        max_info = [1, 0]

        while que:
            node, sum_distance = que.popleft()

            end_trigger = True
            for next_node, next_distance in G[node]:
                if not visited[next_node]:
                    end_trigger = False
                    visited[next_node] = True
                    que.append([next_node, sum_distance + next_distance])

            if end_trigger:
                if sum_distance > max_info[1]:
                    max_info = [node, sum_distance]

        return max_info

    reverse_node, result = bfs(1)
    _, result = bfs(reverse_node)

    print(result)