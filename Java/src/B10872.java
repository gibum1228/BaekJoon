/*
����
0���� ũ�ų� ���� ���� N�� �־�����. �̶�, N!�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� ���� N(0 �� N �� 12)�� �־�����.
���
ù° �ٿ� N!�� ����Ѵ�.
 */
import java.util.Scanner;

public class B10872 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // n! �Է¹ޱ�
		
		System.out.println(fac(n));
		
		sc.close();
	}
	
	static int fac(int f) { // ���丮�� ����Լ�
		if(f == 0) { // n�� 1�̸� 1��ȯ
			return 1;
		}else {
			return f * fac(f-1); // f * (f-1)!
		}
	}
}