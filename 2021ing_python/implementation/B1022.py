import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    # 위, 오, 아, 왼
    move_r = [-1, 0, 1, 0]
    move_c = [0, 1, 0, -1]

    r1, c1, r2, c2 = map(int, IN().split())
    view = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
    total_count = (c2 - c1 + 1) * (r2 - r1 + 1)
    head = 1 # 머리 방향
    now_r, now_c = 0, 0
    num = 1 # 소용돌이 순서
    count = 1 # 같은 방향으로 전진 할 횟수 -> 회전을 2번 할 때마다 +1
    max_len = 0

    while total_count > 0:
        for _ in range(2):
            for _ in range(count):
                if r1 <= now_r <= r2 and c1 <= now_c <= c2:
                    view[now_r - r1][now_c - c1] = num
                    total_count -= 1
                    max_len = num

                now_r += move_r[head]
                now_c += move_c[head]
                num += 1

            # 턴하기
            head = (head - 1) % 4

        # 2번 회전 시 전진 횟수 증가
        count += 1

    max_len = len(str(max_len))
    for i in range(r2 - r1 + 1):
        for j in range(c2 - c1 + 1):
            print(str(view[i][j]).rjust(max_len), end=" ")
        print()