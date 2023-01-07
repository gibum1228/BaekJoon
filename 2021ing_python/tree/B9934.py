import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    K = int(IN())
    tree = {
        k: [] for k in range(1, K+1)
    }
    visit_seq = list(map(int, IN().rstrip().split()))

    def search(arr, level):
        if level > K:
            return

        mid = len(arr) // 2
        tree[level].append(arr[mid])

        search(arr[:mid], level+1)
        search(arr[mid:], level+1)

    search(visit_seq, 1)

    for k, v in tree.items():
        print(*v)