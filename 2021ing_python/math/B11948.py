if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    F = int(input())

    print((sum([A, B, C, D]) - min(A, B, C, D)) + max(E, F))