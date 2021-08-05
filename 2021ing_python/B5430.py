import sys
from collections import deque


if __name__ == '__main__':
    T = int(sys.stdin.readline().rstrip())

    for _ in range(T):
        '''
            p: 수행할 함수들
            n: 배열의 길이
            arr: 수가 담긴 배열
        '''
        p = list(sys.stdin.readline().rstrip())
        n = int(sys.stdin.readline().rstrip())
        arr = input()[1:-1].split(',')
        on_left = True  # 왼오 트리거 -> 처음은 왼쪽 기준임
        error = False # 에러 판단 트리거

        if arr[0] != '': # 빈 배열이 아니면
            dq = deque(list(map(int, arr)))
        else: # 빈 배열이면
            dq = deque([])

        for order in p: # 수행할 함수
            if order == "R": # R은 숫자의 순서를 뒤집음
                on_left = not on_left # 그래서 트리거 온오프
            else:
                if len(dq) == 0: # 함수가 D인데 배열의 크기가 0이라면
                    error = True # 에러 발생
                    break
                else:
                    if on_left: # 왼쪽 첫번째 숫자 삭제
                        dq.popleft()
                    else: # 오른쪽 첫번째 숫자 삭제
                        dq.pop()

        if error: # 에러면
            print("error")
        else: # error 상태가 아니면 리스트 프린트
            results = list(dq)
            if not on_left: # 왼쪽이 아니라 오른쪽이 기준이면
                results.reverse()

            print(f"[{','.join(list(map(str, results)))}]") # 출력 형식에 맞게 출력