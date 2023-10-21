import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    K = int(IN())

    def count_below(number):
        count = 0

        for row in range(1, N + 1):
            count += min((number - 1) // row, N) # number보다 작은 값 개수 구하기

        return count

    left, right = 0, N * N # 최소값에서 최대값
    while left <= right:
        middle = (left + right) // 2

        # middle이 몇 번째로 작은 수 인지 확인
        if count_below(middle) >= K: # K 번째 보다 큰 수라면 왼쪽에서 탐색
            right = middle - 1
        else: # K 번째 보다 작은 수라면 오른쪽에서 탐색
            left = middle + 1

    print(right)