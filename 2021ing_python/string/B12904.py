import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    S = IN().rstrip()
    T = IN().rstrip()
    que = deque(list(T))

    back = 'R'
    head = 'L'
    while (que[0] in ['A', 'B']) and (que[-1] in ['A', 'B']):
        # 문자열 뒤에 A 삭제
        if back == 'R' and que[-1] == 'A':
            que.pop()
        elif back == 'L' and que[0] == 'A':
            que.popleft()
        # print(que, "|", head, back)
        # break
        if len(S) == len(que):
            break

        # 문자열 뒤집고 앞에 B 추가
        if back == 'R' and que[-1] == 'B':
            que.pop()
            head = 'R'
            back = 'L'
        elif back == 'L' and que[0] == 'B':
            que.popleft()
            head = 'L'
            back = 'R'
        # print(que, "|", head, back)
        # break
        if len(S) == len(que):
            break

    result = ''.join(que)
    if head == 'R':
        result = result[::-1]

    print(1 if result == S else 0)