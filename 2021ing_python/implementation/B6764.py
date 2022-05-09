if __name__ == "__main__":
    arr = [int(input()) for i in range(4)]

    no_fish = False

    for i in arr:
        if 1 < arr.count(i) < 4:
            no_fish = True
            break

    if arr.count(arr[0]) == 4:
        print("Fish At Constant Depth")
    elif no_fish:
        print("No Fish")
    elif arr == sorted(arr):
        print("Fish Rising")
    elif arr == sorted(arr, reverse=True):
        print("Fish Diving")
    else:
        print("No Fish")