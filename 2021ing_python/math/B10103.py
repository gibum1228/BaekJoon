import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    a, b = 0, 0

    for _ in range(int(IN())):
        a_score, b_score = map(int, IN().split())

        if a_score != b_score:
            if a_score < b_score:
                a += b_score
            else:
                b += a_score

    print(100 - a)
    print(100 - b)