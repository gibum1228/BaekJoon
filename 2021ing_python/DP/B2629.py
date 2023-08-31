import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    c = int(IN())
    c_weight = list(map(int, IN().split()))
    check = int(IN())
    check_weight = list(map(int, IN().split()))
    dp = [[0 for _ in range(30*500+1)] for _ in range(c+1)]
    results = set()

    def logic(c_weight, c, now_c, left, right):
        now_weight = abs(left - right)

        if now_weight not in results:
            results.add(now_weight)

        if c == now_c:
            return

        if dp[now_c][now_weight] == 0:
            logic(c_weight, c, now_c + 1, left + c_weight[now_c], right)
            logic(c_weight, c, now_c + 1, left, right + c_weight[now_c])
            logic(c_weight, c, now_c + 1, left, right)
            dp[now_c][now_weight] = 1

    logic(c_weight, c, 0, 0, 0)

    answer = []
    for check_x in check_weight:
        if check_x in results:
            answer.append("Y")
        else:
            answer.append("N")

    print(*answer)