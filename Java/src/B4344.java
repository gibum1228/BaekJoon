/*
����
���л� ��������� 90%�� �ڽ��� �ݿ��� ����� �Ѵ´ٰ� �����Ѵ�. ����� �׵鿡�� ���� ������ �˷���� �Ѵ�.
�Է�
ù° �ٿ��� �׽�Ʈ ���̽��� ���� C�� �־�����.
��° �ٺ��� �� �׽�Ʈ ���̽����� �л��� �� N(1 �� N �� 1000, N�� ����)�� ù ���� �־�����, �̾ N���� ������ �־�����. 
������ 0���� ũ�ų� ����, 100���� �۰ų� ���� �����̴�.
���
�� ���̽����� �� �پ� ����� �Ѵ� �л����� ������ �ݿø��Ͽ� �Ҽ��� ��° �ڸ����� ����Ѵ�.
 */
import java.util.Scanner;

public class B4344 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		// ����� �Ѵ� �л����� ������ avgUpCount / studentCount * 100
		int sum; // ���� ����
		int avg; // ���
		double avgUpCount; // ��� �Ѵ� �л� ��
		int classCount = sc.nextInt(); // �б� ����
		int[][] gradeArray = new int [classCount][1000]; // �б� �� 2���� �迭
		
		for(int i = 0; i < classCount; i++) {
			sum = 0; // �ʱ�ȭ
			avg = 0;
			avgUpCount = 0;
			int studentCount = sc.nextInt(); // �б� �ο� ��
			
			for(int j = 0; j < studentCount; j++) { // �б� �ο� ����� ���� ä���
				gradeArray[i][j] = sc.nextInt();
			}
			
			for(int k = 0; k < studentCount; k++) { // ���� ���ϱ�
				sum += gradeArray[i][k];
			}
			
			avg = sum / studentCount; // ��� ���ϱ�
			
			for(int l = 0; l < studentCount; l++) { // ����� �Ѵ� �л� �� ���ϱ�
				if(gradeArray[i][l] > avg) {
					avgUpCount++;
				}
			}
			
			double answer = (avgUpCount / (double)studentCount) * 100.0; // ���� ���ϱ�
			
			System.out.printf("%.3f%%\n", answer); // print
		}
		
		sc.close();
	}

}
