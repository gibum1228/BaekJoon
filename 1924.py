"""
문제
오늘은 2007년 1월 1일 월요일이다. 그렇다면 2007년 x월 y일은 무슨 요일일까? 이를 알아내는 프로그램을 작성하시오.
입력
첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다. 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
출력
첫째 줄에 x월 y일이 무슨 요일인지에 따라 SUN, MON, TUE, WED, THU, FRI, SAT중 하나를 출력한다.
"""
x, y = input().split() # x월 y일 입력받기
x = int(x) # int형변환
y = int(y) # int형변환
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 리스트에 달 별로 일 수 저장
sum = 0 # x달 까지 일 수를 저장하기 위한 sum 초기화

if x == 1 : # 1월이라면
    day = y % 7 # 7로 나눈 나머지를 day에 저장
else : # 1월이 아니면
    for i in range(0, x - 1) : # 0 ~ x-1 까지
        sum += month[i] # 지나온 달의 일 수를 sum에 저장
    day = (sum + y) % 7 # sum + y 를 한 후 7로 나눈 나머지를 day에 저장

if day == 0 : # 나머지가 0이면
    print("SUN") # 일요일
elif day == 1 : # 나머지가 1이면
    print("MON") # 월요일
elif day == 2 : # 나머지가 2이면
    print("TUE") # 화요일
elif day == 3 : # 나머지가 3이면
    print("WED") # 수요일
elif day == 4 : # 나머지가 4이면
    print("THU") # 목요일
elif day == 5 : # 나머지가 5이면
    print("FRI") # 금요일
elif day == 6 : # 나머지가 6이면
    print("SAT") # 토요일