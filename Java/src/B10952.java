/*
����
�� ���� A�� B�� �Է¹��� ����, A+B�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
�Է��� ���� ���� �׽�Ʈ ���̽��� �̷���� �ִ�.
�� �׽�Ʈ ���̽��� �� �ٷ� �̷���� ������, �� �ٿ� A�� B�� �־�����. (0 < A, B < 10)
�Է��� ���������� 0 �� ���� ���´�.
���
�� �׽�Ʈ ���̽����� A+B�� ����Ѵ�.
 */
import java.util.Scanner;

public class B10952 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			if((a == 0) && (b == 0)) {
				break;
			}
			
			System.out.println(a+b);
		}
		
		sc.close();
	}

}
