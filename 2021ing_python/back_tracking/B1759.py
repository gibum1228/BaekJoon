import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    L, C = map(int, IN().split())
    words = sorted(list(IN().split()))
    s = []

    def back_tracking():
        if len(s) == L:
            vo, co = 0, 0

            for i in range(L):
                if s[i] in 'aeiou':
                    vo += 1
                else:
                    co += 1

            if vo >= 1 and co >= 2:
                print("".join(s))

            return


        for w in words:
            if len(s) == 0:
                s.append(w)
                back_tracking()
                s.pop()
            elif w > s[len(s) - 1]:
                s.append(w)
                back_tracking()
                s.pop()

    back_tracking()