"""
문제
정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오
입력
첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
"""
n, x = input().split()
n = int(n)
x = int(x)
l = input().split()

for i in l :
    i = int(i)
    if i >= x :
        continue
    print(i, end = " ")

n, x = input().split() # n과 x를 동시에 입력받고 공백을 기준으로 나누기
n = int(n) # n을 int형으로 변환
x = int(x) # x를 int형으로 변환
L = input() # L을 입력받기
list_L = L.split(" ", n-1) # 입력받은 것을 n-1만큼 공백을 기준으로 나누기
i = 0 # i를 초기화
z = "" # z를 초기화
while i < n : # i가 n보다 작으면 반복
    if int(list_L[i]) < x : # L[i]에 있는 숫자가 x보다 작으면
        z += list_L[i] + " " # z에 L[i]와" " 넣기
    i += 1 # i에 1만큼 추가
print(z) # z를 출력