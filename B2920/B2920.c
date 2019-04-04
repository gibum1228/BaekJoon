/*
문제
다장조는 c d e f g a b C, 총 8개 음으로 이루어져있다. 이 문제에서 8개 음은 다음과 같이 숫자로 바꾸어 표현한다. c는 1로, d는 2로, ..., C를 8로 바꾼다.
1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
입력
첫째 줄에 8개 숫자가 주어진다. 이 숫자는 문제 설명에서 설명한 음이며, 1부터 8까지 숫자가 한 번씩 등장한다.
출력
첫째 줄에 ascending, descending, mixed 중 하나를 출력한다.
*/
#include<stdio.h>

int main() {
	int melody[8]; // 멜로디 입력받을 배열 선언

	scanf("%d %d %d %d %d %d %d %d", &melody[0], &melody[1], &melody[2], &melody[3], &melody[4], &melody[5], &melody[6], &melody[7]); // 한 줄에 8개 입력받기

	if (melody[0] == 1) { // 첫 음이 1일 경우
		int n = 1; // 음계를 확인할 변수 n
		for (int i = 0; i < 8; i++) {
			if (melody[i] != n) { // 1-8 순서대로 있지 않으면
				printf("mixed");
				break;
			}
			n++;
			if (i == 7) { // 마지막까지 이상없으면 ascending 출력
				printf("ascending");
			}
		}
	}
	if (melody[0] == 8) { // 첫 음이 8일 경우
		int n = 8; // 음계를 확인할 변수 n
		for (int i = 0; i < 8; i++) {
			if (melody[i] != n) { // 8-1 순서대로 있지 않을 경우
				printf("mixed");
				break;
			}
			n--;
			if (i == 7) {
				printf("descending");
			}
		}
	}
	if(!(melody[0] == 8 || melody[0] == 1)){ // 첫 음이 1 또는 8이 아니라면
		printf("mixed");
	}

	return 0;
}