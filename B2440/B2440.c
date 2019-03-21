/*
문제:
첫째 줄에는 별 N개, 둘째 줄에는 별 N-1개, ..., N번째 줄에는 별 1개를 찍는 문제
입력:
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력:
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
*/
#include<stdio.h>

int main() {
	int N;
	int i;
	int j;

	scanf("%d", &N); // N 입력 받기

	for (i = 0; i < N; i++) {
		for (j = i; j < N; j++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}