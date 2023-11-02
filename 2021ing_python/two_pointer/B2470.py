import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arr = sorted(list(map(int, IN().split())))
    left, right = 0, N-1
    global_diff = float('inf')
    results = [None, None]

    while left < right:
        diff = arr[left] + arr[right]

        if abs(diff) < global_diff:
            global_diff = abs(diff)
            results = [arr[left], arr[right]]
            if global_diff == 0:
                break

        if diff < 0:
            left += 1
        else:
            right -= 1

    print(*sorted(results))