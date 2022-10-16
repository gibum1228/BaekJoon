import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    stack = []
    result = ""

    for _ in range(int(IN())):
        line = IN().rstrip().split(" ")

        if line[0] == "push":
            stack.append(line[1])
        else:
            if line[0] == "pop":
                result += stack.pop() if stack else "-1"
            elif line[0] == "size":
                result += str(len(stack))
            elif line[0] == "empty":
                result += "0" if stack else "1"
            elif line[0] == "top":
                result += stack[len(stack) - 1] if stack else '-1'

            result += "\n"

    print(result)