import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    num = list(map(int, IN().rstrip().split()))
    op = list(map(int, IN().rstrip().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈
    current_count = [0] * 4
    min_num, max_num = 10**9, -(10**9)

    def dfs(value, current_count):
        global min_num, max_num

        for n in num[1:]:
            if current_count[0] < op[0]: # 덧셈
                current_count[0] += 1
                value = value + n
            elif current_count[1] < op[1]: # 뺄셈
                current_count[1] += 1
                value = value - n
            elif current_count[2] < op[2]: # 곱셈
                current_count[2] += 1
                value = value * n
            elif current_count[3] < op[3]: # 나눗셈
                current_count[3] += 1
                value = value // n
            else:
                min_num = min(min_num, value)
                max_num = max(max_num, value)
                return

            dfs(value, current_count)

    dfs(num[0], current_count)

    print(min_num)
    print(max_num)