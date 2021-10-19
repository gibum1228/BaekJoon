import sys
sys.setrecursionlimit(10**9)


class Node:
    def __init__(self, key: int, left = None, right = None):
        self.key = key
        self.left = left
        self.right = right

    def insertNode(self, key):
        if self.key > key:
            if self.left:
                self.left.insertNode(key)
            else:
                self.left = Node(key)
                return
        else:
            if self.right:
                self.right.insertNode(key)
            else:
                self.right = Node(key)
                return

    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        if self.key != -1:
            print(self.key)


if __name__ == "__main__":
    root = Node(-1)

    while True:
        try:
            root.insertNode(int(sys.stdin.readline().rstrip()))
        except:
            break

    root.postOrder()