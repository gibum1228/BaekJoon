/*
����
�� ���� A�� B�� �Է¹��� ����, A+B�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� �׽�Ʈ ���̽��� ���� T�� �־�����.
�� �׽�Ʈ ���̽��� �� �ٷ� �̷���� ������, �� �ٿ� A�� B�� �־�����. (0 < A, B < 10)
���
�� �׽�Ʈ ���̽����� "Case #x: A + B = C" �������� ����Ѵ�. x�� �׽�Ʈ ���̽� ��ȣ�̰� 1���� �����ϸ�, C�� A+B�̴�.
 */
import java.util.Scanner;

public class B11022 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt(); // �׽�Ʈ ���̽� ũ���� t �Է¹ޱ�
		
		for(int i = 1; i <= t; i++) { // t��ŭ �ݺ�
			int a = sc.nextInt(); // a, b �Է¹ޱ�
			int b= sc.nextInt();
			
			System.out.println("Case #" + i + ": " + a + " + " + b + " = " + (a+b)); // i�� ���̽� ��ȣ ǥ���� a+b�� ���
		}
		
		sc.close();
	}

}