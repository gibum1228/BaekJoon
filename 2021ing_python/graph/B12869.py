import sys
from collections import deque
from itertools import permutations

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    SCVs = list(map(int, IN().split()))
    case = [9, 3, 1]
    cases = list(permutations(case[:len(SCVs)], r=len(SCVs)))


    que = deque([SCVs + [0]])
    visited = {tuple(SCVs)}
    while que:
        info = que.popleft()

        for x in cases:
            new_list = []
            trigger = True

            for i in range(N):
                new_list.append(info[i] - x[i])

                if new_list[-1] > 0:
                    trigger = False

            if tuple(new_list) in visited:
                continue
            else:
                visited.add(tuple(new_list))

            new_list.append(info[-1] + 1)

            if trigger:
                print(new_list[-1])
                exit()
            else:
                que.append(new_list)