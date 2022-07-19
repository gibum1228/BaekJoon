import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    char = IN().rstrip()

    if char == 'n' or char == 'N':
        print("Naver D2")
    else:
        print("Naver Whale")