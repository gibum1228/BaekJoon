import sys
from collections import Counter, deque

IN = sys.stdin.readline

if __name__ == "__main__":
    S = IN().rstrip()
    counter = Counter(S)
    que = deque()

    # 홀수 찾기
    for k, v in counter.items():
        if v % 2 == 1:
            if not que:
                que.append(k)
            else:
                print("I'm Sorry Hansoo")
                exit()

    # 팰린드롬 만들기
    for k, v in sorted(counter.items(), reverse=True):
        for i in range(v//2):
            que.append(k)
            que.appendleft(k)

    # 출력
    print(''.join(que))