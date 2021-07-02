N = int(input())

for _ in range(N):
    r, e, c = map(int, input().split())
    e -= c

    if e > r:
        print("advertise")
    elif e < r:
        print("do not advertise")
    else:
        print("does not matter")