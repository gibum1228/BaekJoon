import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A = IN().rstrip()
    B = IN().rstrip()

    if len(A) >= len(B):
        print("go")
    else:
        print("no")