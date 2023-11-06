import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    A = list(map(int, IN().split()))

    list_arr = [-1000000001]
    list_total = [(-1000000001, 0)]
    A = A[::-1]

    while A:
        a = A.pop()

        if a > list_arr[-1]:
            list_total.append((a, len(list_arr)))
            list_arr.append(a)
        else:
            left, right = -1, len(list_arr)

            while left + 1 < right:
                mid = (left + right) // 2

                if a > list_arr[mid]:
                    left = mid
                else:
                    right = mid

            list_arr[right] = a
            list_total.append((a, right))

    results = []
    length = len(list_arr) - 1
    while list_total and length:
        num, idx = list_total.pop()

        if idx == length:
            results.append(num)
            length -= 1

    print(len(results))
    print(*results[::-1])