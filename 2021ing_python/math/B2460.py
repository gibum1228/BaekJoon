import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    result = 0
    count = 0

    for _ in range(10):
        out_, in_ = map(int, IN().split())
        count = count + (in_ - out_)
        result = max(result, count)

    print(result)