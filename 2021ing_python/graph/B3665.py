import sys
from collections import deque
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    for T in range(int(IN())):
        N = int(IN())
        G = {}
        in_degree = {}

        # 그래프 만들기
        original = set([i for i in range(1, N+1)])
        for x in list(map(int, IN().split())):
            original.remove(x)
            G[x] = copy.deepcopy(original)
            in_degree[x] = (N - 1) - len(original)

        # update G
        try:
            for M in range(int(IN())):
                a, b = map(int, IN().split())

                if in_degree[a] > in_degree[b]: # a가 b보다 순위가 높다면
                    a = a
                    b = b
                elif in_degree[a] < in_degree[b]: # a가 b보다 순위가 낮다면
                    tmp = a
                    a = b
                    b = tmp

                G[b].remove(a) # 순위가 뒤로 간 애
                G[a].add(b) # 순위가 앞으로 간 애
        except:
            print("IMPOSSIBLE")
            continue

        # update in_degree
        for x in range(1, N+1):
            in_degree[x] = (N - 1) - len(G[x])

        # find start point
        que = deque([])
        check_rank_duplication = [False for _ in range(N)]
        continue_trigger = False
        for x in range(1, N+1):
            rank = in_degree[x]

            if rank == 0:
                que.append(x)

            if check_rank_duplication[rank]:
                continue_trigger = True
                break
            else:
                check_rank_duplication[rank] = True

        if continue_trigger: # 동일한 순위가 여러 명이라 확실한 순서를 찾을 수 없음
            print("IMPOSSIBLE")
            continue

        # 위상 절렬
        results = []
        while que:
            node = que.pop()
            results.append(node)

            for next_node in G[node]:
                in_degree[next_node] -= 1

                if in_degree[next_node] == 0:
                    que.append(next_node)

        print(*results)