if __name__ == "__main__":
    T = int(input())

    five_m = T // 300
    T %= 300

    one_m = T // 60
    T %= 60

    ten_s = T // 10
    T %= 10

    if T == 0:
        print(five_m, one_m, ten_s)
    else:
        print(-1)