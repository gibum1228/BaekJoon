import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, IN().split())
    number = IN().rstrip()
    stack = []

    for num in number:
        while stack and stack[-1] < num and k > 0:
            stack.pop()
            k -= 1

        stack.append(num)

    if k > 0:
        print(''.join(stack[:-k]))
    else:
        print(''.join(stack))