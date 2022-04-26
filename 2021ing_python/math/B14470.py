if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    results = 0

    if A < 0:
        results += (C * abs(A))
        A = 0

    if A == 0:
        results += D

    B -= A
    results += (E * B)

    print(results)