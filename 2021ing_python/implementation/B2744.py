import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    input_str = IN().rstrip()
    result = ""

    for s in input_str:
        if s.isupper():
            result += s.lower()
        else:
            result += s.upper()

    print(result)