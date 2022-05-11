if __name__ == "__main__":
    y, m, d = map(int, input().split())
    sy, sm, sd = map(int, input().split())

    if sm < m or (sm == m and sd < d):
        print(sy - y - 1)
    else:
        print(sy - y)

    print(1 + (sy - y))
    print(sy - y)