if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    LIS = [0]

    for n in arr:
        if LIS[-1] < n:
            LIS.append(n)
        else:
            left = 0
            right = len(LIS)

            while left < right:
                mid = (left + right) // 2

                if LIS[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            LIS[right] = n

    print(len(LIS) - 1)