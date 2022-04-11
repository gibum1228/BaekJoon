if __name__ == "__main__":
    K, N, M = map(int, input().split())

    remainder = min(M - (K * N), 0)

    print(abs(remainder))