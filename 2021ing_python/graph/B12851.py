def bfs(N, K):
    time = 0
    que = [N]
    new_que = []

    while True:
        if que.count(K) > 0:
            count = que.count(K)
            break

        time += 1
        while que:
            now = que.pop(0)
            visited[now] = True

            if now-1 >= 0:
                if not visited[now-1]:
                    new_que.append(now-1)
            if now+1 <= 100000:
                if not visited[now+1]:
                    new_que.append(now+1)
            if now*2 <= 100000:
                if not visited[now*2]:
                    new_que.append(now*2)

        que = new_que
        new_que = []

    return time, count


if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [False] * 100001

    time, count = bfs(N, K)

    print(time)
    print(count)