import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())

    for _ in range(T):
        s = IN().rstrip()
        print(s[0] + s[len(s)-1])