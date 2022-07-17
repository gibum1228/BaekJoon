import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    call_time = list(map(int, IN().rstrip().split()))
    y, m = 0, 0

    for i in call_time:
        y += i // 30 * 10 + 10
        m += i // 60 * 15 + 15

    if y < m:
        print('Y', y)
    elif y > m:
        print('M', m)
    else:
        print('Y M', y)
