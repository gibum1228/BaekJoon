import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    count = 0
    result = -1

    for _ in range(6):
        WorL = IN().rstrip()

        if WorL == "W":
            count += 1

    if count >= 5:
        result = 1
    elif count >= 3:
        result = 2
    elif count >= 1:
        result = 3

    print(result)