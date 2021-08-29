import sys


def bfs(start, end):
    que = [start]
    next_que = []
    time = 0
    count = 0
    
    while que:
        focus = que.pop(0)
        if focus == end:  # break
            count += 1 + que.count(end) # end 갯수를 구해 가장 빠른 시간으로 찾는 방법이 몇 가지인지를 구함
            break
        elif focus == 0:  # 0일 경우 +1만 가능
            checking(focus + 1, end, next_que)
        elif focus == 100000:  # 100,000일 경우 -1만 가능
            checking(focus - 1, end, next_que)
        elif focus * 2 > 100000:  # 현재값 * 2가 범위를 넘어갈 경우
            checking(focus - 1, end, next_que)
            checking(focus + 1, end, next_que)
        else:  # default
            checking(focus - 1, end, next_que)
            checking(focus * 2, end, next_que)
            checking(focus + 1, end, next_que)

        # 현재 스택이 끝나면 다음 스택으로 넘어감 and time++
        if not que:
            que = next_que.copy()
            next_que = []
            time += 1

    if time == 0:
        count = 0

    return time, count


# 이미 한 번 확인한 숫자라면 큐에 새로 들어가지 않음
def checking(num, end, next_que):
    if num == end: # 단, 찾으려는 숫자는 count하기 위해 추가
        next_que.append(num)
    elif not check[num]:
        check[num] = True
        next_que.append(num)


if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    check = [False for _ in range(100001)]  # 숫자 중복 확인 방지
    check[N] = True

    time, count = bfs(N, M)

    print(time)
    print(count)
