"""
문제:
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.
S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.
입력:
첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다.
S의 길이는 적어도 1이며, 20글자를 넘지 않는다.
출력:
각 테스트 케이스에 대해 P를 출력한다.
"""
T = int(input()) # 테스트 케이스 정의

result = [] # 최종값 저장할 result 초기화
for i in range(0, T):
    s = input() # 'R S' 출력받기
    o = "" # 각 패턴마다 초기화하기 위해 for문 안에서 정의
    R = int(s[0]) # 문자 R번만큼 출력하기
    for j in range(2, len(s)): # 문자 한 개씩 R번 만큼 o에 대입하기
        o += s[j] * R # 조건에 맞는 문자열 생성
    result.append(o) # result에 저장

for i in range(0, T):
    print(result[i]) # 조건에 맞는 result 출력