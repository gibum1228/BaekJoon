import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    T = int(IN())

    for _ in range(T):
        x, y = map(int, IN().split())

        d = y - x # 거리
        n = 0

        while True:
            if d <= n * (n + 1):
                break
            n += 1

        if d <= n**2: # 총 이동 거리가 n의 제곱보다 작거나 같을 때
            print(n * 2 - 1)
        else: # 총 이동 거리가 n의 제곱보다 클 때
            print(n*2)