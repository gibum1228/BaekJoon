import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    name = IN().rstrip()
    output = [[":fan:" for _ in range(3)] for _ in range(3)]
    output[1][1] = f":{name}:"

    for row in output:
        print("".join(row))