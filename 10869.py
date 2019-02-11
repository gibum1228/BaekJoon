"""
문제:
두 자연수 A와 B가 주어진다.
이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.
입력:
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
출력:
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
"""
a, b = map(int, input().split()) # 한 줄에 두 개의 수 입력 받기

print(a+b) # 더하기
print(a-b) # 빼기
print(a*b) # 곱하기
print(a//b) # 몫
print(a%b) # 나머지