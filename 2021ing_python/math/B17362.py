if __name__ == "__main__":
    n = int(input())

    if n <= 5:
        print(n)
    else:
        n -= 5
        s = n // 4
        r = n % 4

        if s % 2 == 0:
            print(5 - r)
        else:
            print(r + 1)