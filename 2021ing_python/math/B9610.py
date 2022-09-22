import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    one, two, three, four, axis = 0, 0, 0, 0, 0

    for _ in range(int(IN())):
        x, y = map(int, IN().split())

        if x == 0 or y == 0:
            axis += 1
        elif x > 0 and y > 0:
            one += 1
        elif x < 0 and y > 0:
            two += 1
        elif x < 0 and y < 0:
            three += 1
        elif x > 0 and y < 0:
            four += 1

    print("Q1:", one)
    print("Q2:", two)
    print("Q3:", three)
    print("Q4:", four)
    print("AXIS:", axis)