import sys
import copy
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    A, B = map(int, IN().split())

    def bfs(start):
        global B
        que = deque([start])
        new_que = deque()
        visited = set([start])
        count = 0

        while que:
            if B in que:
                return count

            x = que.popleft()
            case1 = x * 2
            case2 = int(str(x) + "1")

            if not case1 in visited and case1 <= B:
                new_que.append(case1)
                visited.add(case1)
            if not case2 in visited and case2 <= B:
                new_que.append(case2)
                visited.add(case2)

            if not new_que:
                return -1

            if not que:
                que = copy.deepcopy(new_que)
                new_que = deque()
                count += 1

    result = bfs(A)

    print(result + 1 if result != -1 else result)