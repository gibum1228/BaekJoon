# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

# 첫째 줄에 시험 점수가 주어진다. 시험 점수는 0보다 크거나 같고, 100보다 작거나 같은 자연수이다.

score = int(input()) # 점수 입력받기

if(score >= 90) :
    print("A") # 100점 또는 90점대 A
elif(score >= 80) :
    print("B") # 80점대 B
elif(score >= 70) :
    print("C") # 70점대 C
elif(score >= 60) :
    print("D") # 60점대 D
else :
    print("F") # 60점 미만 F