import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def append(self, parents, index):
        if self.key == parents:
            if not self.left: # find left child or right child
                self.left = Node(index)
            else:
                self.right = Node(index)
            return

        if self.left:
            self.left.append(parents, index)
        if self.right:
            self.right.append(parents, index)

    def remove(self, target):
        if self.left:
            if self.left.key == target:
                self.left = None
                return
            self.left.remove(target)
        if self.right:
            if self.right.key == target:
                self.right = None
                return
            self.right.remove(target)


    def search(self):
        if not self.left and not self.right: # plus
            global count
            if self.key == 0:
                count = 0
            else:
                count += 1

        if self.left:
            self.left.search()
        if self.right:
            self.right.search()

if __name__ == '__main__':
    # input
    N = sys.stdin.readline()
    node_list = list(map(int, sys.stdin.readline().split()))
    remove_target = int(sys.stdin.readline())

    # init
    node = Node(0)
    count = 0

    if remove_target == 0:
        print(0)
    else:
        # create tree
        for i in range(1, len(node_list)):
            if node_list[i] != -1:
                node.append(node_list[i], i)
        # remove node
        node.remove(remove_target)
        # calculate count
        node.search()
        # print
        print(count)