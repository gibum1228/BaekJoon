import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    label2num = {k: v for v, k in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])}
    move = {
        'R': (0, 1), 'L': (0, -1), # R: 한 칸 오른쪽으로, L: 한 칸 왼쪽으로
        'B': (1, 0), 'T': (-1, 0), # B: 한 칸 아래로, T: 한 칸 위로
        'RT': (-1, 1), 'LT': (-1, -1), # RT: 오른쪽 위 대각선으로, LT: 왼쪽 위 대각선으로
        'RB': (1, 1), 'LB': (1, -1) # RB: 오른쪽 아래 대각선으로, LB: 왼쪽 아래 대각선으로
    }

    # 킹, 돌의 시작 위치와 N 입력 받기
    king, stone, N = IN().rstrip().split()
    king, stone = list(king), list(stone)
    king_x, king_y = 8 - int(king[1]), label2num[king[0]]
    stone_x, stone_y = 8 - int(stone[1]), label2num[stone[0]]
    # 이동 명령어
    for _ in range(int(N)):
        order = IN().rstrip()
        move_x, move_y = move[order]

        next_king_x = king_x + move_x
        next_king_y = king_y + move_y

        # 이동 가능한 범위라면
        if 0 <= next_king_x < 8 and 0 <= next_king_y < 8:
            # 이동 위치에 돌이 있는 경우
            if next_king_x == stone_x and next_king_y == stone_y:
                next_stone_x = stone_x + move_x
                next_stone_y = stone_y + move_y

                # 돌이 밖으로 안 나가는 경우, 돌과 킹 동시 이동
                if 0 <= next_stone_x < 8 and 0 <= next_stone_y < 8:
                    king_x = next_king_x
                    king_y = next_king_y
                    stone_x = next_stone_x
                    stone_y = next_stone_y
            else: # 이동 위치에 돌이 없는 경우, 킹만 이동
                king_x = next_king_x
                king_y = next_king_y

    num2label = {k:v for k, v in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])}
    print(f"{num2label[king_y]}{8 - king_x}")
    print(f"{num2label[stone_y]}{8 - stone_x}")