/*
����
�� ���� A�� B�� �Է¹��� ����, A+B�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� �׽�Ʈ ���̽��� ���� T�� �־�����.
�� �׽�Ʈ ���̽��� �� �ٷ� �̷���� ������, �� �ٿ� A�� B�� �־�����. (0 < A, B < 10)
���
�� �׽�Ʈ ���̽����� A+B�� ����Ѵ�.
 */
import java.util.Scanner;

public class B10950 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int[] ab = new int[2];
		int size = sc.nextInt();
		
		for(int i = 0; i < size; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			ab[0] = a;
			ab[1] = b;
			
			System.out.println(a + b);
		}
		
		sc.close();
	}

}
