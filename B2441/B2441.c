/*
����
ù° �ٿ��� �� N��, ��° �ٿ��� �� N-1��, ..., N��° �ٿ��� �� 1���� ��� ����
������, �������� �������� ������ ��(���� ����)�� ����Ͻÿ�.
�Է�
ù° �ٿ� N(1 �� N �� 100)�� �־�����.
���
ù° �ٺ��� N��° �ٱ��� ���ʴ�� ���� ����Ѵ�.
*/
#include<stdio.h>

int main() {
	int N;

	scanf("%d", &N);

	for (int i = 0; i < N; i++) {
		for (int k = 0; k < i; k++) {
			printf(" ");
		}
		for (int j = N - i; j > 0; j--) {
			printf("*");
		}
		printf("\n");
	}

	return 0;
}