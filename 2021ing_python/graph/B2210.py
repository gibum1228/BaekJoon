import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    visited = dict()
    G = []
    for _ in range(5):
        G.append(list(map(str, IN().split())))

    def dfs(r, c, word):
        if len(word) == 6:
            visited[word] = 1
            return

        for mr, mc in move:
            next_r = r + mr
            next_c = c + mc

            if 0 <= next_r < 5 and 0 <= next_c < 5:
                dfs(next_r, next_c, word + G[next_r][next_c])

    for r in range(5):
        for c in range(5):
            dfs(r, c, '')

    print(len(visited))