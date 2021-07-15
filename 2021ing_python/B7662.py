import heapq
import sys
input = sys.stdin.readline


# 동기화 메소드
def sync(q):
    # min_que, max_que 동기화
    while q and not id[q[0][1]]:
        print("sync -----")
        print(q[0])
        print(min_que)
        print(max_que)
        heapq.heappop(q)
        print(min_que)
        print(max_que)

if __name__ == "__main__":
    for T in range(int(input())):
        k = int(input())
        max_que, min_que = [], []
        id = [False] * 1000001 # 동기화 아이디

        for i in range(k):
            order, num = input().split()

            if order == 'I':
                # input
                heapq.heappush(min_que, (int(num), i))
                heapq.heappush(max_que, (-int(num), i))
                id[i] = True
                print("insert -----")
                print(min_que)
                print(max_que)
            elif num == '1':
                print("max sync")
                sync(max_que)

                # 최대값 삭제
                if max_que:
                    id[max_que[0][1]] = False
                    heapq.heappop(max_que)
            else:
                print("min sync")
                sync(min_que)

                # 최소값 삭제
                if min_que:
                    id[min_que[0][1]] = False
                    heapq.heappop(min_que)

        sync(min_que)
        sync(max_que)

        # print
        if max_que and min_que:
            print(-max_que[0][0], min_que[0][0])
        else:
            print("EMPTY")