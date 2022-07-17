import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    answer = list(map(int, IN().rstrip().split()))
    score = []
    num = 0

    for i in range(len(answer)):
        if answer[i] == 1:
            num += 1
            score.append(num)
        else:
            num = 0

    print(sum(score))