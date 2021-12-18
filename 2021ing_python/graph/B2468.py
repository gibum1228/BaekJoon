import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    borad = [list(map(int, IN().split())) for _ in range(N)]
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    safe_zone = -1

    def bfs(i, j, h):
        count_zone = 0
        que = [(i, j)]

        while que:


        return count_zone

    for h in range(1, 101):
        visited = [[False for _ in range(N)] for _ in range(N)]
        count_zone = 0
        for i in range(N):
            for j in range(N):
                if not visited[i][j]:
                    bfs(i, j, h)