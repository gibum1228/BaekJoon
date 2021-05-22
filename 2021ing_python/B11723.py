import sys

m = int(sys.stdin.readline())
s = set()

for i in range(m):
    action = sys.stdin.readline().strip().split()

    if len(action) == 1:
        if action[0] == "all":
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        action, x = action[0], action[1]
        x = int(x)

        if action == "add":
            s.add(x)
        elif action == "remove":
            s.discard(x)
        elif action == "check":
            print(1 if x in s else 0)
        elif action == "toggle":
            if x in s:
                s.discard(x)
            else:
                s.add(x)