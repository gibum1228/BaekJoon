import sys

if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    result = [0, 0]
    min_num = sys.maxsize

    # 1
    left, right = 0, len(arr) - 1
    while left < right:
        sum_num = arr[left] + arr[right]

        # 2
        if abs(sum_num) < min_num:
            result[0], result[1] = arr[left], arr[right]
            min_num = abs(sum_num)

        # 3
        if sum_num < 0:
            left += 1
        elif sum_num > 0:
            right -= 1
        else:
            break

    print(*result)