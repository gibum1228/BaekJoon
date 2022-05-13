if __name__ == "__main__":
    D, H, M = map(int, input().split())

    start = 11 * 60 + 11
    end = ((D - 11) * 24 * 60) + H * 60 + M

    if end - start >= 0:
        print(end - start)
    else:
        print(-1)