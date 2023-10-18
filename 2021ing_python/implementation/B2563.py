import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    canvas = [[False for _ in range(100)] for _ in range(100)] # False is white, True is black
    count = 0

    for _ in range(int(IN())):
        w, h = map(int, IN().split())

        for r in range(w-1, w+10-1):
            for c in range(h-1, h+10-1):
                if not canvas[r][c]:
                    canvas[r][c] = True
                    count += 1

    print(count)