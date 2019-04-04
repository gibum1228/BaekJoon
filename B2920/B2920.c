/*
����
�������� c d e f g a b C, �� 8�� ������ �̷�����ִ�. �� �������� 8�� ���� ������ ���� ���ڷ� �ٲپ� ǥ���Ѵ�. c�� 1��, d�� 2��, ..., C�� 8�� �ٲ۴�.
1���� 8���� ���ʴ�� �����Ѵٸ� ascending, 8���� 1���� ���ʴ�� �����Ѵٸ� descending, �� �� �ƴ϶�� mixed �̴�.
������ ������ �־����� ��, �̰��� ascending����, descending����, �ƴϸ� mixed���� �Ǻ��ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� 8�� ���ڰ� �־�����. �� ���ڴ� ���� ������ ������ ���̸�, 1���� 8���� ���ڰ� �� ���� �����Ѵ�.
���
ù° �ٿ� ascending, descending, mixed �� �ϳ��� ����Ѵ�.
*/
#include<stdio.h>

int main() {
	int melody[8]; // ��ε� �Է¹��� �迭 ����

	scanf("%d %d %d %d %d %d %d %d", &melody[0], &melody[1], &melody[2], &melody[3], &melody[4], &melody[5], &melody[6], &melody[7]); // �� �ٿ� 8�� �Է¹ޱ�

	if (melody[0] == 1) { // ù ���� 1�� ���
		int n = 1; // ���踦 Ȯ���� ���� n
		for (int i = 0; i < 8; i++) {
			if (melody[i] != n) { // 1-8 ������� ���� ������
				printf("mixed");
				break;
			}
			n++;
			if (i == 7) { // ���������� �̻������ ascending ���
				printf("ascending");
			}
		}
	}
	if (melody[0] == 8) { // ù ���� 8�� ���
		int n = 8; // ���踦 Ȯ���� ���� n
		for (int i = 0; i < 8; i++) {
			if (melody[i] != n) { // 8-1 ������� ���� ���� ���
				printf("mixed");
				break;
			}
			n--;
			if (i == 7) {
				printf("descending");
			}
		}
	}
	if(!(melody[0] == 8 || melody[0] == 1)){ // ù ���� 1 �Ǵ� 8�� �ƴ϶��
		printf("mixed");
	}

	return 0;
}