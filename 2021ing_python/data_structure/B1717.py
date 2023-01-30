import sys

IN = sys.stdin.readline


def find(arr, n):
    if arr[n] != n:
        arr[n] = find(arr, arr[n])
    return arr[n]


def union(arr, a, b):
    parent_a = find(arr, a)
    parent_b = find(arr, b)
    arr[parent_b] = parent_a


if __name__ == "__main__":
    n, m = map(int, IN().split())
    arr = [i for i in range(n + 1)]

    for _ in range(m):
        order, a, b = map(int, IN().split())

        if order == 0:
            union(arr, a, b)
        else:
            if find(arr, a) == find(arr, b):
                print("YES")
            else:
                print("NO")
