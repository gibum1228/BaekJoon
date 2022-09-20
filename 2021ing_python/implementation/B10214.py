import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        y, k = 0, 0

        for __ in range(9):
            score_y, score_k = map(int, IN().split())
            y += score_y
            k += score_k

        if y == k:
            print("Draw")
        elif y > k:
            print("Yonsei")
        else:
            print("Korea")