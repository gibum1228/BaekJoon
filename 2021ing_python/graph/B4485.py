import sys
import heapq

IN = sys.stdin.readline

if __name__ == "__main__":
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    i = 1
    while True:
        N = int(IN()) # N x N 동굴
        if N == 0: break # N이 0이면 게임 종료

        # 도둑루피 크기가 담긴 동굴
        board = []
        for _ in range(N):
            board.append(list(map(int, IN().split())))

        # 최단 경로 저장
        distance = [[float('inf') for _ in range(N)] for _ in range(N)]
        que = [(0, 0, board[0][0])]

        while que:
            row, col, weight = heapq.heappop(que)

            # 기존에 기록된 최단 경로가 더 짧다면 더이상 볼 필요가 없음
            if distance[row][col] < weight:
                continue

            # 인접한 상하좌우로 이동할지 말지 결정
            for mr, mc in move:
                next_row, next_col = row + mr, col + mc

                if 0 <= next_row < N and 0 <= next_col < N:
                    next_weight = weight + board[next_row][next_col]

                    if next_weight < distance[next_row][next_col]: # 최단 경로면 갱신 후 큐에 삽입
                        distance[next_row][next_col] = next_weight
                        heapq.heappush(que, (next_row, next_col, next_weight))

        print(f"Problem {i}: {distance[N-1][N-1]}")
        i += 1