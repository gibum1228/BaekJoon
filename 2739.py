"""
구구단 출력하기
"""
N = int(input()) # 단 수 N을 입력받기

for i in range(1, 10) : # i는 1부터 9까지
    print("%d * %d = %d" %(N, i, N*i)) # N단 출력