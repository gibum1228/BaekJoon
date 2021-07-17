import sys

class Node:
    key = None
    left = None
    right = None

    # constructor
    def __init__(self, value, left=".", right="."):
        self.key = value
        if left != '.':
            self.left = Node(left)
        if right != '.':
            self.right = Node(right)

    # find root
    def find_tree(self, value, left, right):
        if self.key == value:
            self.left = Node(left)
            self.right = Node(right)

        if self.left is not None:
            self.left.find_tree(value, left, right)

        if self.right is not None:
            self.right.find_tree(value, left, right)
    
    # 전위 순회
    def first_traversal(self):
        if self.key != '.':
            print(self.key, end="")

        if self.left is not None:
            self.left.first_traversal()

        if self.right is not None:
            self.right.first_traversal()

    # 중위 순회
    def middle_traversal(self):
        if self.left is not None:
            self.left.middle_traversal()

        if self.key != '.':
            print(self.key, end="")

        if self.right is not None:
            self.right.middle_traversal()

    # 후위 순회
    def last_traversal(self):
        if self.left is not None:
            self.left.last_traversal()

        if self.right is not None:
            self.right.last_traversal()

        if self.key != '.':
            print(self.key, end="")

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    tree = Node('A')

    # input
    for _ in range(N):
        k, l, r = sys.stdin.readline().split()
        tree.find_tree(k, l, r)

    # logic
    tree.first_traversal()
    print()
    tree.middle_traversal()
    print()
    tree.last_traversal()