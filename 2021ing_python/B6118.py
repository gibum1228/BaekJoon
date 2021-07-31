import sys

def bfs(room):
    que = [1] # 현재 노드들, 시작점은 1
    visited[1] = True
    next_que = [] # 다음 노드들
    copy = [] # 최종 큐 목록
    count = 0 # bfs 진행한 횟수

    while que:
        index = que.pop(0) # 현재 포커싱 노드 번호

        for value in room[index]: # 현재 포커싱 노드와 연결된 노드 목록 중에서
            if not visited[value]: # 방문 안 한 노드가 있다면
                visited[value] = True # 방문 체크 후
                next_que.append(value) # 다음 방문 예정에 추가

        if not que and next_que: # 현재 BFS(que)를 끝내고 다음 턴의 BFS(next_que)을 할 차례라면
            copy = next_que.copy() # 마지막 노드 목록 기록 -> 다음 턴의 BFS가 없다면 현재 if는 실행되지 않음
            que = next_que.copy()
            next_que = []
            count += 1

    return f"{min(copy)} {count} {len(copy)}"

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().rstrip().split())
    room = [[] for _ in range(N+1)]
    visited = [False for _ in range(N+1)]

    # create room
    for i in range(M):
        A_i, B_i = map(int, sys.stdin.readline().rstrip().split())

        room[A_i].append(B_i)
        room[B_i].append(A_i)

    # result print
    print(bfs(room))