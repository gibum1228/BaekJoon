import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    num = list(map(int, IN().rstrip().split()))
    op = list(map(int, IN().rstrip().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈
    current_count = [0] * 4
    min_num, max_num = 10**9, -(10**9)

    def dfs(value, current_count, start):
        global min_num, max_num, N, num

        for n in range(start, N):
            for i in range(4):
                if current_count[i] < op[i]:
                    if i == 0:
                        current_count[i] += 1
                        n_value = value + num[n]
                        print("=====")
                        print(f"{n}({value})에서 연산자{i} => {n_value}")
                        dfs(n_value, current_count, n+1)
                        current_count[i] -= 1
                    elif i == 1:
                        current_count[i] += 1
                        n_value = value - num[n]
                        print("=====")
                        print(f"{n}({value})에서 연산자{i} => {n_value}")
                        dfs(n_value, current_count, n+1)
                        current_count[i] -= 1
                    elif i == 2:
                        current_count[i] += 1
                        n_value = value * num[n]
                        print("=====")
                        print(f"{n}({value})에서 연산자{i} => {n_value}")
                        dfs(n_value, current_count, n+1)
                        current_count[i] -= 1
                    else:
                        current_count[i] += 1
                        n_value = -(-value // num[n]) if value < 0 else value // num[n]
                        print("=====")
                        print(f"{n}({value})에서 연산자{i} => {n_value}")
                        dfs(n_value, current_count, n+1)
                        current_count[i] -= 1

        if start == N:
            min_num = min(min_num, value)
            max_num = max(max_num, value)

    dfs(num[0], current_count, 1)

    print("=====")
    print(max_num)
    print(min_num)