import sys


def calc(num, value):
    while(num > 0):
        results[num % 10] += value
        num = num // 10


def logic(start, end, num):
    while start % 10 and start <= end:
        calc(start, num)

        start += 1

    if start > end:
        return

    while end % 10 != 9 and start <= end:
        calc(end, num)

        end -= 1

    count = end // 10 - start // 10 + 1
    for i in range(len(results)):
        results[i] += count * num

    logic(start//10, end//10, num*10)


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    results = [0 for _ in range(10)]

    logic(1, N, 1)

    for i in results:
        print(i, end=" ")