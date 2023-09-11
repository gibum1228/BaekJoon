import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    problem = list(IN().rstrip())
    stack = []
    result = ''

    for s in problem:
        if s.isalpha():
            result += s
        else:
            if s == '(':
                stack.append(s)
            elif s == "*" or s == "/":
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    result += stack.pop()
                stack.append(s)
            else:
                while stack and stack[-1] != '(':
                    result += stack.pop()

                if s == ')':
                    stack.pop()
                else:
                    stack.append(s)

    while stack:
        result += stack.pop()

    print(result)