import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.child = []

    def append(self, parents, index):
        if self.key == parents:
            self.child.append(Node(index)) # find left child or right child
            return

        if self.child: # 자식이 있으면
            for child_node in self.child: # 자식 중에서 parents를 key로 가진 노드 찾기
                child_node.append(parents, index)

    def delete(self, target):
        for i in range(len(self.child)): # child 길이 만큼
            if self.child[i].key == target: # i번째 child가 삭제할 타겟이면 삭제
                self.child.pop(i)
                return
            else: # 아니면 다음 자식들 중에서 target 찾기
                self.child[i].delete(target)

    def search(self):
        if not self.child: # 리프 노드(자식이 없음)
            global count
            count += 1
            return

        if self.child: # 자식들을 기준으로 탐색
            for child_node in self.child:
                child_node.search()

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
        node.delete(remove_target)
        # calculate count
        node.search()

        # print
        print(count)