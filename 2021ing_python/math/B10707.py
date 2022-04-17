if __name__ == "__main__":
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    P = int(input())

    print(min((A * P), (B if P < C else B + (P - C) * D)))