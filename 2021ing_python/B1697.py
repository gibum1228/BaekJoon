import sys

def bfs(start, end):
    que = [start]
    next_que = []
    count = 0

    while len(que) != 0:
        focus = que.pop(0)

        if focus == end: # break
            return count
        elif focus == 0: # 0일 경우 +1만 가능
            checking(focus + 1, next_que)
        elif focus == 100000: # 100,000일 경우 -1만 가능
            checking(focus - 1, next_que)
        elif focus * 2 > 100000: # 현재값 * 2가 범위를 넘어갈 경우
            checking(focus - 1, next_que)
            checking(focus + 1, next_que)
        else: # default
            checking(focus - 1, next_que)
            checking(focus * 2, next_que)
            checking(focus + 1, next_que)

        # 현재 스택이 끝나면 다음 스택으로 넘어감 and count++
        if len(que) == 0:
            que = next_que.copy()
            next_que = []
            count += 1

# 이미 한 번 확인한 숫자라면
def checking(num, next_que):
    if not check[num]:
        check[num] = True
        next_que.append(num)

if __name__ == "__main__":
    start, end = map(int, sys.stdin.readline().split())
    check = [False for _ in range(100001)] # 숫자 중복 확인 방지
    check[start] = True

    print(bfs(start, end))