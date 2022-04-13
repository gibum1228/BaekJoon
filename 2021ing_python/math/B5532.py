if __name__ == "__main__":
    L = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())

    c1 = A // C if A % C == 0 else A // C + 1
    c2 = B // D if B % D == 0 else B // D + 1

    print(L - max(c1, c2))