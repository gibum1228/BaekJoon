"""
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""
C = int(input()) # 테스트케이스 C의 갯수 입력받기

avr = [] # 평균 리스트 초기화
result = [] # 비율 리스트 초기화

for i in range(0, C) : # 0~C-1까지 반복
    num = input().split() # 한 줄의 학생의 수와 점수 입력받기
    kkk = int(num[0]) # kkk의 학생의 수 저장
    sum = 0 # 학생들 점수의 합을 저장하는 sum 초기화
    count = 0 # 평균을 넘는 학생을 저장하는 count 초기화
    for j in range(1, kkk + 1) : # 1~kkk 까지 반복
        num[j] = int(num[j]) # num리스트를 int형으로 변환
        sum += num[j] # sum에 학생들 점수 더하기
    avr.append(sum/kkk) # sum을 학생들의 수(kkk)로 나눠 평균 저장
    for k in range(1, kkk + 1) : # 비율따지기
        if avr[i] < num[k] : # k번째 학생의 점수가 평균보다 높으면
            count += 1 # 카운트 추가
    result.append((count/kkk) * 100) # 평균 넘은 학생 수 / 학생 수를 백분율로 만들기 위ㅐ X100

for i in range(0, C) : # 비율 출력
    print("%.3f%%" %result[i]) # "%" 나타내기 위해 %% 사용