import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())

    tree = list(map(int, IN().rstrip().split()))

    tree.sort(reverse=True)

    for i in range(len(tree)):
        tree[i] = tree[i] + i + 1

    print(max(tree) + 1)