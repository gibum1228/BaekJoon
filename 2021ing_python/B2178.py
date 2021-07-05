def BFS(N, M, blocks, queue, visited):
    count = 0 # 이동 횟수

    while not visited[N][M] and queue:
        next_research = [] # 다음으로 탐색할 위치 정보
        count += 1 # 횟수++

        for pos in queue:
            i = pos[0]
            j = pos[1]

            # 방문 하지 않은 장소라면
            if not visited[i][j]:
                # 방문 체크
                visited[i][j] = True
                # 4 방향 중 어디로 갈 지 체크
                if blocks[i+1][j] == 1 and not visited[i+1][j]:
                    next_research.append([i+1, j])
                if blocks[i][j+1] == 1 and not visited[i][j+1]:
                    next_research.append([i, j+1])
                if blocks[i][j-1] == 1 and not visited[i][j-1]:
                    next_research.append([i, j-1])
                if blocks[i-1][j] == 1 and not visited[i-1][j]:
                    next_research.append([i-1, j])
        # 너비 우선 탐색 갱신
        queue = next_research.copy()

    return count

if __name__ == "__main__":
    N, M = map(int, input().split()) # (N, M)
    blocks = [[0 for _ in range(M+2)] for _ in range(N+2)] # 미로 블록 정보
    queue = [[1, 1]] # BFS 큐
    visited = [[False for _ in range(M+2)] for _ in range(N+2)] # 방문 여부

    # input
    for i in range(1, N + 1):
        blocks[i] = list(map(int, list(input())))
        blocks[i].insert(0, 0)
        blocks[i].insert(M+1, 0)

    print(BFS(N, M, blocks, queue, visited))