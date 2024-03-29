import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    n = int(IN())
    x, y = [], []
    answer = 0

    for _ in range(n):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    # 마지막 점과 시작 점의 면적을 구하기 위해 맨 뒤에 시작점을 추가함
    x, y = x + [x[0]], y + [y[0]]

    # 신발끈 정리 적용
    for i in range(n):
        answer += (x[i] * y[i + 1]) - (x[i + 1] * y[i])

    print(round(abs(answer) / 2, 1))