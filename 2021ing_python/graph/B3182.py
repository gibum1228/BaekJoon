import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arr = [0]

    for _ in range(N):
        arr.append(int(IN()))

    def dfs(start, count):
        visited[start] = True

        count += 1

        if not visited[arr[start]]:
            count = dfs(arr[start], count)

        return count

    result = -1
    max_count = -1

    for i in range(1, N+1):
        visited = [False] * (N+1)

        now = dfs(i, 0)

        if now > max_count:
            result = i
            max_count = now
        elif now == max_count:
            if i < result:
                result = i

    print(result)