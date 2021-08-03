import sys


class Dice:
    def __init__(self):
        self.left = 0
        self.right = 0
        self.top = 0
        self.bottom = 0
        self.front = 0
        self.back = 0

    '''
        map_value: 이동한 후에 지도 값
        operator: 동(1), 서(2), 북(3), 남(4)
    '''
    def moving(self, order):
        if order == 1:
            left, right, top, bottom = self.bottom, self.top, self.left, self.right
            self.left, self.right, self.top, self.bottom = left, right, top, bottom
        elif order == 2:
            left, right, top, bottom = self.top, self.bottom, self.right, self.left
            self.left, self.right, self.top, self.bottom = left, right, top, bottom
        elif order == 3:
            front, back, top, bottom = self.top, self.bottom, self.back, self.front
            self.front, self.back, self.top, self.bottom = front, back, top, bottom
        else:
            front, back, top, bottom = self.bottom, self.top, self.front, self.back
            self.front, self.back, self.top, self.bottom = front, back, top, bottom


if __name__ == "__main__":
    N, M, x, y, K = map(int, sys.stdin.readline().rstrip().split())
    board = [[] for _ in range(N)]
    dice = Dice()
    move = [(0, 1), (0, -1), (-1, 0), (1, 0)]

    # create board(map)
    for i in range(N):
        board[i] = list(map(int, sys.stdin.readline().rstrip().split()))

    # position (i, j)
    i, j = x, y
    # processing order
    orders = list(map(int, sys.stdin.readline().rstrip().split()))
    for order in orders:
        dx, dy = i + move[order - 1][0], j + move[order - 1][1] # 이동한 후에 좌표값
        if (0 <= dx < N) and (0 <= dy < M):
            i, j = dx, dy # 이동한 좌표값이 범위 내라면 좌표값 저장
            if board[dx][dy] == 0: # 현재 보드 값이 0이면 bottom을 board[dx][dy]에 복사
                dice.moving(order)
                print(dice.top)
                board[dx][dy] = dice.bottom
            else: # 현재 보드 값이 0이 아니면, bottom에 현재 보드 값 복사 후 보드 값 0으로 만들기
                dice.moving(order)
                print(dice.top)
                dice.bottom = board[dx][dy]
                board[dx][dy] = 0