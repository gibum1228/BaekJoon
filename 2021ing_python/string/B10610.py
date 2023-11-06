import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = sorted(list(IN().rstrip()), reverse=True)

    result = -1
    if '0' in N:
        sum_num = 0

        for s in N:
            sum_num += int(s)

        if sum_num % 3 == 0:
            result = ''.join(N)

    print(result)