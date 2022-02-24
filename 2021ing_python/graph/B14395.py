import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    s, t = map(int, IN().split())
    visited = []
    stack = [(s, "")]

    if s == t:
        print(0)
        exit()

    while True:
        num, text = stack.pop(0)

        if num == t:
            print(text)
            break

        if not visited.count(num * num):
            stack.append((num * num, text + "*"))

        if not visited.count(num + num):
            stack.append((num + num, text + "+"))

        if not visited.count(num - num):
            stack.append((num - num, text + "-"))

        if num != 0 and not visited.count(num / num):
            stack.append((num * num, text + "/"))
