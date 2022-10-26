import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    df = [0, 1, 2, 4, 7]
    for i in range(5, 12): # df[i]는 i-1, i-2, i-3의 합이다
        df.append(df[i-1] + df[i-2] + df[i-3])

    for T in range(int(IN())): # T번 만큼 작동
        N = int(IN()) # [1, 2, 3]의 합으로 N을 만들 수 있는 경우의 수 구하기

        print(df[N])