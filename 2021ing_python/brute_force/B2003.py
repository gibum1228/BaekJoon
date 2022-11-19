import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    arr = list(map(int, IN().split()))
    answer = 0
    left, right = 0, 1

    while left <= right and right <= N:
        focus = arr[left:right]
        num = sum(focus)

        if num == M:
            answer += 1
            right += 1
        elif num > M:
            left += 1
        else:
            right += 1

    print(answer)