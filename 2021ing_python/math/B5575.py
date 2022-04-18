if __name__ == "__main__":
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    for sh, sm, ss, eh, em, es in [A, B, C]:
        h = eh - sh
        m = em - sm
        s = es - ss

        if s < 0:
            m -= 1
            s += 60

        if m < 0:
            h -= 1
            m += 60

        print(h, m, s)