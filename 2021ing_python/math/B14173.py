import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    rect1 = list(map(int, IN().rstrip().split()))
    rect2 = list(map(int, IN().rstrip().split()))

    print(max((max(rect1[2], rect2[2]) - min(rect1[0], rect2[0])), (max(rect1[3], rect2[3]) - min(rect1[1], rect2[1])))**2)