import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, C, E = map(int, IN().split())
    sa, sc, se = map(int, IN().split())

    if sa >= A and sc >= C and se >= E:
        print("A")
    elif sa >= A / 2 and sc >= C and se >= E:
        print("B")
    elif sc >= C and se >= E:
        print("C")
    elif sc >= C / 2 and se >= E / 2:
        print("D")
    else:
        print("E")