import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    H, W = map(int, IN().split())
    heights = list(map(int, IN().split()))

    ### draw board
    board = [[False for _ in range(W)] for _ in range(H)]
    for col, h in enumerate(heights):
        for row in range(h):
            board[row][col] = True

    ### find water
    water_count = 0
    for row in range(H):
        wall_index = []

        for col, x in enumerate(board[row]):
            if x:
                wall_index.append(col)

        for i in range(len(wall_index)-1):
            count = wall_index[i+1] - wall_index[i] - 1

            if count > 0:
                water_count += count

    print(water_count)