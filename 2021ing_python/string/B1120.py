import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B = IN().rstrip().split()
    results = []

    for i in range(len(B) - len(A) + 1):
        count = 0

        for a, b in zip(A, B[i:i+len(A)]):
            if a != b:
                count += 1

        results.append(count)

    print(min(results))