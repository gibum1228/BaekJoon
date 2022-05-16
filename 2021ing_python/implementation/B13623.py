import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    arr = list(map(int, IN().split()))
    dict = {
        0: "A", 1: "B", 2: "C"
    }

    if sum(arr) == 0 or sum(arr) == 3:
        print("*")
    else:
        if arr.count(0) == 1:
            print(dict[arr.index(0)])
        elif arr.count(1) == 1:
            print(dict[arr.index(1)])
