/*
����
�־��� �� N�� �߿��� �Ҽ��� �� ������ ã�Ƽ� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù �ٿ� ���� ���� N�� �־�����. N�� 100�����̴�. �������� N���� ���� �־����µ� ���� 1,000 ������ �ڿ����̴�.
���
�־��� ���� �� �Ҽ��� ������ ����Ѵ�.
 */
import java.util.Scanner;

public class B1978 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int[] b = new int [a];
		int count = 0;
		int counttotal = 0;
		
		for(int i = 0; i < a; i++) {
			b[i] = sc.nextInt();
		}
		
		for(int i = 0; i < a; i++) {
			for(int j = 1; j <= b[i]; j++) {
				if(b[i] % j == 0) {
					count++;
				}
			}
			if(count == 2) {
				counttotal++;
			}
			count = 0;
		}
		
		System.out.println(counttotal);
		
		sc.close();
	}

}
