def logic(x, y, visited): # (x, y), 중복 방지 + 지나온 경로 길이 확인하는 visited
    global max_count # 전역 변수
    limit = 0

    for m in range(4):
        # 좌표 이동
        i = x + move[m][0]
        j = y + move[m][1]

        # 이동 범위를 넘기지 않고, 같은 알파벳이 적힌 칸은 두 번 지나갈 수 없다
        if ((0 <= i < R) and (0 <= j < C)) and (board[i][j] not in visited):
            logic(i, j, visited + board[i][j]) # 다음 방향으로 나아가기
        else:
            limit += 1 # 어떤 방향으로 가려다가 막힘

    if limit == 4: # 이동할 곳이 없다면 이동 값 비교
        max_count = max(max_count, len(visited))


if __name__ == '__main__':
    # init
    R, C = map(int, input().split())
    board = [list(input()) for _ in range(R)]
    move = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 상우하좌
    max_count = 0 # result

    # logic
    logic(0, 0, board[0][0])

    # print
    print(max_count)
