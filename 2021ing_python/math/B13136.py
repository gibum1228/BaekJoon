if __name__ == "__main__":
    R, C, N = map(int, input().split())

    print((R // N if R % N == 0 else R // N + 1) * (C // N if C % N == 0 else C // N + 1))