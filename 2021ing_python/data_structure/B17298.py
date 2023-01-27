import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    A = list(map(int, IN().split()))
    answer = [-1] * N
    stack = [0]

    for i in range(1, N):
        while stack and A[stack[-1]] < A[i]:
            answer[stack.pop()] = A[i]
        stack.append(i)

    print(*answer)