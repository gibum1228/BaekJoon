/*
����
(�� �ڸ� ��) �� (�� �ڸ� ��)�� ������ ���� ������ ���Ͽ� �̷������.
(1)�� (2)��ġ�� �� �� �ڸ� �ڿ����� �־��� �� (3), (4), (5), (6)��ġ�� �� ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� (1)�� ��ġ�� �� �� �ڸ� �ڿ�����, ��° �ٿ� (2)�� ��ġ�� �� ���ڸ� �ڿ����� �־�����.
���
ù° �ٺ��� ��° �ٱ��� ���ʴ�� (3), (4), (5), (6)�� �� ���� ����Ѵ�.
 */
import java.util.Scanner;

public class B2588 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int num1 = sc.nextInt(); // (1)
		int num2 = sc.nextInt(); // (2)
		
		int mul1 = num1 * (num2 % 100  % 10); // (3)
		int mul2 = num1 * (num2 % 100 / 10); // (4)
		int mul3 = num1 * (num2 / 100); // (5)
		
		int result = mul1 + (mul2 * 10) + (mul3 * 100); // (6)
		
		System.out.println(mul1);
		System.out.println(mul2);
		System.out.println(mul3);
		System.out.println(result);
		
		sc.close();
	}

}
