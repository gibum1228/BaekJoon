import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    arr = list(IN().rstrip().split())

    if int(arr[0]) + int(arr[2]) == int(arr[4]):
        print("YES")
    else:
        print("NO")