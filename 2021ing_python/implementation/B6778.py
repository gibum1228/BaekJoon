import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A = int(IN())
    B = int(IN())

    if A >= 3 and B <= 4:
        print("TroyMartian")

    if A <= 6 and B >= 2:
        print("VladSaturnian")

    if A <= 2 and B <= 3:
        print("GraemeMercurian")