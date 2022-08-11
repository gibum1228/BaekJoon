import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    Ur, Tr, Uo, To = map(int, IN().split())
    print(56 * Ur + 24 * Tr + 14 * Uo + 6 * To)