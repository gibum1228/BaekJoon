"""
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
입력
첫째 줄에 N이 주어진다. N은 항상 3×2k 수이다. (3, 6, 12, 24, 48, ...) (k ≤ 10)
"""
def star():
    s = '''
       *   
      * *  
     *****'''
    print(s, end = "")

K = 0
N = int(input())
three = 3

N2 = N // 3
while N2 != 1:
    N2 /= 2
    K += 1

for i in range(0, K):
    blankCount = N - three
    print(" " * blankCount, end = "")
    star()
    K -= 1
    for j in range(0, 1):
        blankCount -= three
        print(" " * blankCount, end = "")
        star()
        star()