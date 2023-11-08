import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    M = int(IN())
    S = IN().rstrip()
    pattern = "I" + ("OI" * N)

    # logic
    result = 0
    i = 0
    count = 0
    while i < (M - 1):
        if S[i:i + 3] == 'IOI':
            i += 2
            count += 1
            if count == N:
                result += 1
                count -= 1
        else:
            i += 1
            count = 0

    print(result)