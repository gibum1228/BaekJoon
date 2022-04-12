if __name__ == "__main__":
    h, m, s = map(int, input().split())
    ds = int(input())

    h += ds // 3600
    ds %= 3600
    m += ds // 60
    ds %= 60
    s += ds

    m += s // 60
    s %= 60
    h += m // 60
    m %= 60

    if h > 23:
        h = h % 24
    
    print(h, m, s)