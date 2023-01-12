import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    trigger = [False, False] + [True] * (N-1) # N만큼, 0과 1도 소수 아님
    prime_num = []

    # 에라토스테네스의 체 -> 배수로 소수 찾기
    for i in range(2, N+1):
        if trigger[i]:
            prime_num.append(i)

            for j in range(i*2, N+1, i): # 배수면 약수가 있으니 소수 아님
                trigger[j] = False

    # 투 포인터
    result = 0
    start, end = 0, 0

    while end <= len(prime_num):
        sum_num = sum(prime_num[start:end])

        if sum_num == N:
            result += 1
            end += 1
        elif sum_num < N:
            end += 1
        else:
            start += 1

    print(result)