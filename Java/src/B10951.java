/*
A+B - 4
�ð� ����	�޸� ����	����	����	���� ���	���� ����
1 ��	256 MB	36716	13785	11795	39.719%
����
�� ���� A�� B�� �Է¹��� ����, A+B�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
�Է��� ���� ���� �׽�Ʈ ���̽��� �̷���� �ִ�.
�� �׽�Ʈ ���̽��� �� �ٷ� �̷���� ������, �� �ٿ� A�� B�� �־�����. (0 < A, B < 10)
���
�� �׽�Ʈ ���̽����� A+B�� ����Ѵ�.
 */
import java.util.Scanner;

public class B10951 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNextInt()) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			System.out.println(a+b);
		}
		
		sc.close();
	}

}
