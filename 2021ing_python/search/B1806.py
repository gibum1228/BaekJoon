if __name__ == "__main__":
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))

    # 1
    sum_arr = [0] * (N + 1)
    for i in range(1, N + 1):
        sum_arr[i] = sum_arr[i - 1] + arr[i - 1]

    # 2
    answer = 1000001
    left = 0
    right = 1

    # 3
    while left != N:
        if sum_arr[right] - sum_arr[left] >= S:
            if right - left < answer:
                answer = right - left
            left += 1
        else:
            if right != N:
                right += 1
            else:
                left += 1

    # 4
    if answer != 1000001:
        print(answer)
    else:
        print(0)