import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    V = int(IN())
    arr = list(IN().rstrip())

    a_count = arr.count("A")
    b_count = arr.count("B")

    if a_count > b_count:
        print("A")
    elif b_count > a_count:
        print("B")
    else:
        print("Tie")