import sys
sys.setrecursionlimit(10**9)


def postorder(start, end):
    if start >= end:
        return

    node = preorder[start]

    if preorder[end - 1] <= node:
        postorder(start + 1, end)
        print(node)
        return

    for i in range(start + 1, end):
        if preorder[i] > node:
            idx = i
            break

    postorder(start + 1, idx)
    postorder(idx, end)
    print(node)


if __name__ == "__main__":
    preorder = []

    while True:
        try:
            preorder.append(int(sys.stdin.readline().rstrip()))
        except:
            break

    postorder(0, len(preorder))