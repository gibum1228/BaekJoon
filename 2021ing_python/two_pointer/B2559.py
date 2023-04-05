import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, IN().split())
    arr = list(map(int, IN().split()))
    now_num = sum(arr[:K])
    max_num = now_num

    for i in range(K, N):
        now_num = now_num + arr[i] - arr[i-K]
        max_num = max(max_num, now_num)

    print(max_num)