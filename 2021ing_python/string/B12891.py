import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    S, P = map(int, IN().split())
    DNA = IN().rstrip()
    keys = ['A', 'C', 'G', 'T']
    requirement = {
        k: v for k, v in zip(keys, list(map(int, IN().split()))) # [A, C, G, T]
    }

    # init
    results = 0
    que = deque(DNA[:P-1])
    idx = P-1
    count = {
        k: 0 for k in keys
    }

    for s in que:
        if s in keys:
            count[s] += 1

    while idx < S:
        trigger = True
        que.append(DNA[idx])

        # add
        if que[-1] in keys:
            count[que[-1]] += 1
        # compared
        for key in keys:
            if count[key] < requirement[key]:
                trigger = False
                break
        # check
        if trigger:
            results += 1
        # 왼쪽 거 pop
        idx += 1
        del_word = que.popleft()
        if del_word in keys and count[del_word] > 0:
            count[del_word] -= 1

    print(results)