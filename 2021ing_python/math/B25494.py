import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())

    for _ in range(T):
        count = 0
        a, b, c = map(int, IN().split())

        for x in range(1, a + 1):
            for y in range(1, b + 1):
                for z in range(1, c + 1):
                    if (x % y) == (y % z) == (z % x):
                        count += 1

        print(count)