import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    values = list(map(int, IN().rstrip().split()))
    stack = []
    results = []

    for i in range(N):
        while stack:
            if stack[-1][1] > values[i]:
                results.append(stack[-1][0] + 1)
                break
            else:
                stack.pop()

        if not stack:
            results.append(0)

        stack.append((i, values[i]))

    print(" ".join(map(str, results)))