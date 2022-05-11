import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    arr = sorted(list(map(int, IN().rstrip().split())))

    print("S") if arr[0] == arr[1] or arr[1] == arr[2] or arr[0] + arr[1] == arr[2] else print("N")