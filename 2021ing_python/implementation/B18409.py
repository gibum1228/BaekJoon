import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    S = list(IN().rstrip())
    result = 0

    for x in ['a', 'i', 'u', 'e', 'o']:
        result += S.count(x)

    print(result)