import sys
from collections import Counter

IN = sys.stdin.readline

if __name__ == "__main__":
    arr = sorted([int(IN()) for _ in range(int(IN()))])

    print(int(round(sum(arr) / len(arr), 0)))
    print(arr[len(arr) // 2])
    if len(arr) == 1:
        print(arr[0])
    else:
        a, b = Counter(arr).most_common(2)
        print(a[0] if a[1] != b[1] else b[0])
    print(arr[-1] - arr[0])