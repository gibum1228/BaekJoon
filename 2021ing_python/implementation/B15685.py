import copy
import sys
import copy

IN = sys.stdin.readline

if __name__ == "__main__":
    positions = set() # (x, y)
    move = { # 우상좌하
        0: [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]
    }

    info = []
    for _ in range(int(IN())):
        info.append(list(map(int, IN().split())))

    # create curve
    for r, c, head, level in info:
        positions.add((r, c))

        # 드래곤 커브 그리기
        curve = [head]
        for _ in range(level):
            for i in range(len(curve) - 1, -1, -1):
                curve.append((curve[i] + 1) % 4)

        # 좌표 추가
        for i in curve:
            r, c = r + move[i][0], c + move[i][1]

            positions.add((r, c))

    # 사각형 찾기
    result = 0
    rect_position = set() # 사각형의 맨 왼쪽 좌표만 기억

    for r, c in positions:
        check_rect = True

        for mr, mc in [(0, 1), (1, 0), (1, 1)]:
            if (r + mr, c + mc) not in positions:
                check_rect = False
                break

        if check_rect and (r, c) not in rect_position:
            rect_position.add((r, c))
            result += 1

    print(result)