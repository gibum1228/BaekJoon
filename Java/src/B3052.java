/*
����
�� �ڿ��� A�� B�� ���� ��, A%B�� A�� B�� ���� ������ �̴�. ���� ���, 7, 14, 27, 38�� 3���� ���� �������� 1, 2, 0, 2�̴�. 
�� 10���� �Է¹��� ��, �̸� 42�� ���� �������� ���Ѵ�. �� ���� ���� �ٸ� ���� �� �� �ִ��� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٺ��� ����° �� ���� ���ڰ� �� �ٿ� �ϳ��� �־�����. �� ���ڴ� 1,000���� �۰ų� ����, ���� �ƴ� �����̴�.
���
ù° �ٿ�, 42�� �������� ��, ���� �ٸ� �������� �� �� �ִ��� ����Ѵ�.
 */
import java.util.Scanner;
import java.util.Arrays;

public class B3052 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int count = 1; // ���� �ٸ� ������ ������ ���� ����
		int[] remainder = new int [10]; // 10���� �������� ���� ����
		
		for(int i = 0; i < remainder.length; i++) { // �Է¹��� ������ 42�� ������ ����
			int a = sc.nextInt();
			
			int ab = a % 42;
	
			remainder[i] = ab;
		}
		
		Arrays.sort(remainder); // ����
		
		for(int i = 1; i < remainder.length; i++) { // �������� ������ �ٸ��� ����
			if(i == (remainder.length - 1)) {
				if(remainder[i-1] != remainder[i]) {
					count++;
				}
			}else {
				if(remainder[i-1] != remainder[i]) {
					count++;
				}
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

}
