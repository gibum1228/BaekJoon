import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    for _ in range(int(IN())):
        result = []
        s = bin(int(IN()))[2:]

        for i in range(len(s)):
            if s[i] == "1":
                result.append((len(s) - 1) - i)

        print(" ".join(map(str, result[::-1])))