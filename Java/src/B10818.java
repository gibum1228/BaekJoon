/*
����
N���� ������ �־�����. �̶�, �ּڰ��� �ִ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� ������ ���� N (1 �� N �� 1,000,000)�� �־�����. ��° �ٿ��� N���� ������ �������� �����ؼ� �־�����. ��� ������ -1,000,000���� ũ�ų� ����, 1,000,000���� �۰ų� ���� �����̴�.
���
ù° �ٿ� �־��� ���� N���� �ּڰ��� �ִ��� �������� ������ ����Ѵ�.
 */
import java.util.Scanner;

public class B10818 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt(); // �Է¹��� ���� ����
		
		int[] num = new int [size]; // size ũ���� �迭 ����
		
		for(int i = 0; i < size; i++) { // ���� �Է� �ޱ�
			num[i] = sc.nextInt();
		}
		
		int min = num[0]; // �ּҰ� num[0]���� �ʱ�ȭ
		int max = num[0]; // �ִ� num[0]���� �ʱ�ȭ
		
		for(int i = 1; i < size; i++) { // �ε��� 1������ ������ ���Ͽ� �迭�� �ּҰ��� �ִ� ã��
			if(min > num[i]) {
				min = num[i];
			}
			if(max < num[i]) {
				max = num[i];
			}
		}
		
		System.out.println(min + " " + max); // ����ϱ�
		
		sc.close();
	}

}
