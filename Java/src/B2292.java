/*
����)
���� �׸��� ���� ���������� �̷���� ������ �ִ�. �׸����� ���� �ٿ� ���� �߾��� �� 1���� �����ؼ� �̿��ϴ� �濡 ���ư��鼭 1�� �����ϴ� ��ȣ�� �ּҷ� �ű� �� �ִ�. 
���� N�� �־����� ��, ������ �߾� 1���� N�� ����� �ּ� ������ ���� ������ �� �� �� ���� ���� ����������(���۰� ���� �����Ͽ�)�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�. 
���� ���, 13������ 3��, 58������ 5���� ������.
�Է�)
ù° �ٿ� N(1 �� N �� 1,000,000,000)�� �־�����.
���)
�Է����� �־��� ����� �ּ� ������ ���� ������ �� �� �� ���� ���� �������� ����Ѵ�.
 */
import java.util.Scanner;

public class B2292 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int sum = 1, count = 0;
		int n = sc.nextInt();
		
		for(int i = 0; ; i++) {
			if(sum > n) {
				break;
			}
			sum = sum + (6 * i);
			count++;
		}
		
		System.out.print(count);
		
		sc.close();
	}

}
