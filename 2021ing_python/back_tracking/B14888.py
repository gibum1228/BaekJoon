import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    num = list(map(int, IN().rstrip().split()))
    op = list(map(int, IN().rstrip().split())) # 덧셈, 뺄셈, 곱셈, 나눗셈
    min_num, max_num = 10**9, -(10**9)

    def dfs(value, depth, current_count):
        global max_num, min_num

        if depth == len(num):
            max_num = max(max_num, value)
            min_num = min(min_num, value)
            return
        
        if current_count[0] > 0:
            current_count[0] -= 1
            dfs(value + num[depth], depth+1, current_count)
            current_count[0] += 1
        if current_count[1] > 0:
            current_count[1] -= 1
            dfs(value - num[depth], depth+1, current_count)
            current_count[1] += 1
        if current_count[2] > 0:
            current_count[2] -= 1
            dfs(value * num[depth], depth+1, current_count)
            current_count[2] += 1
        if current_count[3] > 0:
            current_count[3] -= 1
            dfs(value // num[depth] if value > 0 else -(-value // num[depth]), depth+1, current_count)
            current_count[3] += 1

    dfs(num[0], 1, op)
 
    print(max_num)
    print(min_num)