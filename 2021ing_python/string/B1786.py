import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    T = IN().rstrip()
    P = IN().rstrip()
    results = []

    def make_lps():
        length = 0
        i = 1
        lps = [0 for _ in range(len(P))]

        while i < len(P):
            if P[length] == P[i]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length == 0:
                    lps[i] = 0
                    i += 1
                else:
                    length = lps[length - 1]

        return lps

    lps = make_lps()

    i, j = 0, 0
    while i < len(T):
        if T[i] == P[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j-1]

        if j == len(P):
            results.append(i - len(P) + 1)
            j = lps[j-1]

    print(len(results))
    print(*results)