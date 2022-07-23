import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    sum = 0
    min_num = 101

    for i in range(7):
        n = int(IN())

        if n % 2 != 0:
            sum += n
            min_num = min(min_num, n)

    if sum == 0:
        print(-1)
    else:
        print(sum)
        print(min_num)