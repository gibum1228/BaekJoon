import sys

IN = sys.stdin.readline

if __name__ == "__main__":
    N = int(IN())
    arr = list(map(int, IN().split()))
    sort_arr = sorted(set(arr)) # 중복된 수 제거 후 정렬

    dic = {sort_arr[i]: i for i in range(len(sort_arr))} # 좌표 압축 사전화

    s = "" # 문자열로 연결
    for i in arr:
        s += str(dic[i]) + " "

    print(s[:-1])