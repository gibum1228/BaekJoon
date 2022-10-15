import sys
from collections import deque

IN = sys.stdin.readline

if __name__ == "__main__":
    result = ""
    que = deque([])

    for _ in range(int(IN())):
        line = IN().rstrip().split()

        if line[0] == "push":
            que.append(line[1])
        else:
            if line[0] == "pop":
                result += que.popleft() if que else "-1"
            elif line[0] == "size":
                result += str(len(que))
            elif line[0] == "empty":
                result += "0" if que else "1"
            elif line[0] == "front":
                result += que[0] if que else '-1'
            elif line[0] == "back":
                result += que[len(que) - 1] if que else '-1'

            result += "\n"

    print(result)