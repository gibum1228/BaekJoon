import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    N, M = map(int, IN().split())
    zero_position = set()  # 0의 위치 기억
    other_position = set()  # 빙산의 위치 기억
    move = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    G = []  # 지도
    for r in range(N):
        arr = list(map(int, IN().split()))
        G.append(arr)

        for c, n in enumerate(arr):
            if n == 0:
                zero_position.add((r, c))
            else:
                other_position.add((r, c))


    # 두 덩이 이상인 지 확인
    def check(G):
        visited = set()
        visited.update(other_position)
        count = 0

        def bfs(start_r, start_c): # 덩이 갯수 세기
            que = deque([(start_r, start_c)])

            while que:
                r, c = que.popleft()

                for mr, mc in move:
                    next_r = r + mr
                    next_c = c + mc

                    if (next_r, next_c) in visited: # 연결되어 있으면 visited에서 제거
                        visited.discard((next_r, next_c))
                        que.append((next_r, next_c))

        for r, c in other_position:
            if (r, c) in visited:
                count += 1
                bfs(r, c)

        return True if count == 1 else False


    # 빙산 녹이기
    sec = 0
    while check(G):
        next_zero_position = set()  # 녹은 빙산 정보를 담을 리스트

        for r, c in other_position:  # 빙산 주위를 보기 위해 빙산 정보 가져옴
            for mr, mc in move:  # 상하좌우
                if (r + mr, c + mc) in zero_position:  # 빙산 주위가 0이면 빙산 높이 -1
                    G[r][c] = max(0, G[r][c] - 1)  # 음수면 0으로 지정
                if G[r][c] == 0:  # 녹은 빙산 정보 저장
                    next_zero_position.add((r, c))

        if next_zero_position:  # 녹은 빙산 정보를 바탕으로 다른 정보 업데이트
            other_position -= next_zero_position  # 녹은 빙산 정보 빼기
            zero_position.update(next_zero_position)  # 녹은 빙산 정보 추가

        sec += 1

    if len(other_position) == 0:  # 모두 녹았다면
        print(0)
    else:
        print(sec)  # 두 덩이 이상이면