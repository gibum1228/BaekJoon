import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    sentence = IN().rstrip()
    boom = IN().rstrip()

    result = []
    for word in sentence:
        result.append(word)

        if ''.join(result[-len(boom):]) == boom:
            for _ in range(len(boom)):
                result.pop()

    print(''.join(result) if result else "FRULA")