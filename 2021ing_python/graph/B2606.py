def bfs():
    que = [1]
    count = 0
    visited[1] = True

    while que:
        focus = que.pop(0)

        for node in graph[focus]:
            if not visited[node]:
                visited[node] = True
                que.append(node)
                count += 1

    return count


if __name__ == "__main__":
    V = int(input())
    E = int(input())
    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]

    for _ in range(E):
        start, end = map(int, input().split())

        graph[start].append(end)
        graph[end].append(start)

    print(bfs())