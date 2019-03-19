/*
문제:
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제
입력:
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력:
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.
*/
#include <stdio.h>

int main()
{
	int n; // n 변수 생성
	scanf("%d", &n); // 사용자에게 n번째 입력받기
	for (int i = 0; i < n; i++) // n번 만큼
	{
		for (int j = 0; j <= i; j++) // i만큼
		{
			printf("*"); // * 출력
		}
		printf("\n"); // 뉴라인
	}
	return 0;
}