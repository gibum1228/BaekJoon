/*
����>
���� X�� ����� �� �ִ� ������ ������ ���� �� ���� �̴�.
X�� 3���� ������ ��������, 3���� ������.
X�� 2�� ������ ��������, 2�� ������.
1�� ����.
���� N�� �־����� ��, ���� ���� ���� �� ���� ������ ����ؼ� 1�� ������� �Ѵ�. ������ ����ϴ� Ƚ���� �ּڰ��� ����Ͻÿ�.
�Է�>
ù° �ٿ� 1���� ũ�ų� ����, 106���� �۰ų� ���� ���� N�� �־�����.
���>
ù° �ٿ� ������ �ϴ� Ƚ���� �ּڰ��� ����Ѵ�.
 */
import java.util.Scanner;

public class B1463 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int count = 0;
		
		while(n == 1) {
			if(n % 2 == 0) {
				n /= 2;
				count++;
			}else if(n % 3 == 0) {
				n /= 3;
				count++;
			}else {
				n -= 1;
				count++;
			}
		}
		
		System.out.print(count);
			
		sc.close();
	}

}
