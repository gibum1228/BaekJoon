import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    cow = dict()
    result = 0

    for _ in range(int(IN())):
        n, trigger = map(int, IN().split())

        if cow.get(n, -1) == -1:
            cow[n] = trigger
        else:
            if cow[n] != trigger:
                result += 1
                cow[n] = trigger

    print(result)