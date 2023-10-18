import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    S = IN().rstrip()
    stack = []
    tag_trigger = False
    result = ''

    for char in S:
        if char == '<':
            result += ''.join(stack[::-1]) + "<"
            stack = []
            tag_trigger = True
        elif char == '>':
            result += ''.join(stack) + ">"
            stack = []
            tag_trigger = False
        elif char == ' ' and not tag_trigger:
            result += ''.join(stack[::-1]) + ' '
            stack = []
        else:
            stack.append(char)

    result += ''.join(stack[::-1])

    print(result)