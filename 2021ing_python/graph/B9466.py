import sys

sys.setrecursionlimit(10 ** 7)
IN = sys.stdin.readline

if __name__ == "__main__":
    for T in range(int(IN())): # test case
        n = int(IN())
        G = [-1] + list(map(int, IN().split()))
        visited = [False for _ in range(n+1)]
        arr = [] # 팀이 있는 노드들

        def dfs(now_node, cycle):
            global arr
            visited[now_node] = True
            next_node = G[now_node]
            cycle.append(now_node)

            if visited[next_node]:
                if next_node in cycle: # 사이클이면
                    arr += cycle[cycle.index(next_node):] # 유효한 사이클 => 팀
                return
            else:
                dfs(next_node, cycle)

        for i in range(1, n+1):
            if not visited[i]:
                dfs(i, [])

        print(n - len(arr))