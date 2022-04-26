if __name__ == "__main__":
    U = list(map(int, input().split()))

    if sum(U) >= 100:
        print("OK")
    else:
        n = U.index(min(U)) + 1

        if n == 1:
            print("Soongsil")
        elif n == 2:
            print("Korea")
        else:
            print("Hanyang")