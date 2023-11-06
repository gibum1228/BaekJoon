import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    S = IN().rstrip()

    result = {S}
    for window in range(1, len(S)):
        for idx in range(len(S)):
            try:
                result.add(S[idx:idx+window])
            except:
                break

    print(len(result))