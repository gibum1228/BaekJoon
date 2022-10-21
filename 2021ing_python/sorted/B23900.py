import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    A = list(map(int, IN().rstrip().split()))
    B = list(map(int, IN().rstrip().split()))
    trigger = False # 동일 여부 판단

    # 좌표 압축
    pos_dic = {}
    sort_A = sorted(A, reverse=True)
    for i in range(len(A)):
        pos_dic[A[i]] = i

    # 선택 정렬 과정
    last_idx = len(A) - 1 # 맨 뒤 인덱스 -> 정렬되면서 -1씩 됨
    compared_idx = len(A) - 1
    for max_num in sort_A:
        # 배열 비교
        for i in range(compared_idx, -1, -1):
            if A[i] != B[i]: # 중간에 같지 않은게 있다면 중지
                break
            compared_idx = i
            if i == 0: # 끝까지 비교가 됐다면 정답
                trigger = True
        if trigger: break # 정렬문 중지

        # 선택 정렬
        max_idx = pos_dic[max_num]
        pos_dic[max_num], pos_dic[A[last_idx]] = last_idx, max_idx
        A[max_idx], A[last_idx] = A[last_idx], A[max_idx]
        last_idx -= 1

    print(1 if trigger else 0)