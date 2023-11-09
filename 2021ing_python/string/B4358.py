import sys
from collections import defaultdict

IN = sys.stdin.readline

if __name__ == "__main__":
    DB = defaultdict(int)

    total = 0
    while True:
        word = IN().rstrip()

        if word == '':
            break
        else:
            DB[word] += 1
            total += 1

    results = []
    for key in sorted(DB.keys()):
        results.append((key, DB[key] / total * 100))

    for result in results:
        print(result[0], f"{result[1]:>.4f}")