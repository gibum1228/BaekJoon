import copy
from collections import deque

if __name__ == "__main__":
    N = int(input())

    def bfs(num):
        que = deque([(num, num)])
        next_que = deque()
        count = 0
        visited = [False] * (N + 1)
        ori = []

        while que:
            focus_num, parent = que.popleft()
            visited[focus_num] = True
            if focus_num == 1:
                break

            if focus_num % 3 == 0 and not visited[focus_num // 3]:
                visited[focus_num // 3] = True
                next_que.append((focus_num // 3, focus_num))

            if focus_num % 2 == 0 and not visited[focus_num // 2]:
                visited[focus_num // 2] = True
                next_que.append((focus_num // 2, focus_num))

            if not visited[focus_num - 1]:
                visited[focus_num - 1] = True
                next_que.append((focus_num - 1, focus_num))

            if not que:
                ori.append(list(next_que))
                que = copy.deepcopy(next_que)
                next_que = deque()
                count += 1

        return count, ori

    cnt, arr = bfs(N)

    print(cnt)

    result = set([1])
    start = 1
    for i in range(len(arr)-1, -1, -1):
        for x, y in arr[i]:
            if x == start:
                result.add(x)
                result.add(y)
                start = y
    print(*sorted(result, reverse=True))