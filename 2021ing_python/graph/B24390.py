import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    M, S = map(int, IN().split(":"))
    count = 1
    count += (M//10 + M%10)

    if S < 30:
        count += (S//10)
    else:
        count += ((S-30)//10)

    print(count)