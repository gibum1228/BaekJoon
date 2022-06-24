import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    arr = list(map(int, IN().rstrip().split()))
    count = 0
    results = -1

    for i in range(1, N):
        loc = i - 1
        new_item = arr[i]

        while loc >= 0 and new_item < arr[loc]:
            arr[loc + 1] = arr[loc]
            loc -= 1
            count += 1
            if count == K:
                results = arr[loc + 1]
                break

        if loc + 1 != i:
            arr[loc + 1] = new_item
            count += 1
            if count == K:
                results = arr[loc + 1]
                break

    print(results)