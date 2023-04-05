import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    S = int(IN())
    i = 1
    count = 0
    num = 0

    while True:
        num += i
        i += 1

        if  num > S:
            break
        else:
            count += 1

    print(count)