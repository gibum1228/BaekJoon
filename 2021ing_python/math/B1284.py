import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    while True:
        num = IN().rstrip()

        if num == '0':
            break

        result = 2 # 양 옆 공백
        result += len(num) - 1

        for n in list(num):
            if n == '1':
                result += 2
            elif n == '0':
                result += 4
            else:
                result += 3

        print(result)