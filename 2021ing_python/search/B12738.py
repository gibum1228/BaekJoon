if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    LIS = [A[0]]

    # 1
    for n in A[1:]:
        # 2
        if LIS[-1] < n:
            LIS.append(n)
        else: # 3
            left = 0
            right = len(LIS)-1

            # 4
            while left < right:
                mid = (left + right) // 2

                if LIS[mid] < n:
                    left = mid + 1
                else:
                    right = mid

            LIS[right] = n

    print(len(LIS))