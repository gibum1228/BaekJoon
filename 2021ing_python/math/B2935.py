import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    a = int(IN())
    op = IN().rstrip()
    b = int(IN())
    if op == '*':
        print(a * b)
    else:
        print(a + b)