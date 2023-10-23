import sys
from collections import defaultdict

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())

    word_list = []
    db = defaultdict(int)
    for _ in range(N):
        word = IN().rstrip()
        word_list.append(word)

        for idx, char in enumerate(word):
            db[char] += (10**(len(word) - 1 - idx))

    sorted_list = sorted(db.items(), key=lambda x: x[1], reverse=True)

    result = 0
    for idx, (word, value) in enumerate(sorted_list):
        result += value * (9-idx)
    print(result)