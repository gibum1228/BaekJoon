import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    K = int(IN())

    for i in range(1, K + 1):
        info = list(map(int, IN().split()))

        sorted_list = sorted(info[1:], reverse=True)

        diff = 0
        for x in range(len(sorted_list) - 1):
            diff = max(diff, sorted_list[x] - sorted_list[x+1])

        print(f"Class {i}")
        print(f"Max {sorted_list[0]}, Min {sorted_list[len(sorted_list) - 1]}, Largest gap {diff}")