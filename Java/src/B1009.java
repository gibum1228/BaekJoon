import java.util.Scanner;

public class B1009 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tCase = sc.nextInt();
		int a, b, c, result;
		
		for(int i = 0; i < tCase; i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			c = 0; // ���� ���� ���̱� ���� ����
			result = 1;
			
			if(a % 10 == 0 || a % 10 == 1 || a % 10 == 5 || a % 10 == 6) { // 0, 1, 5, 6 �� ������ �ڸ� ����
				result = a % 10;
			}else if( a % 10 == 4 || a % 9 == 9) { // 4, 9�� �� ���� ������ �ڸ� �ٲ�
				c = b % 2;
				if(c == 0) {
					c = 2;
				}
			}else { // �������� 4���� ������ �ڸ��� �ٲ�
				c = b % 4;
				if(c == 0) {
					c = 4;
				}
			}
			
			for(int j = 0; j < c; j++) {
				result = (result * a) % 10;
			}
			
			if(result == 0) { // 0�̸� 10�� ��ǻ�Ͱ� ������ ó��
				result = 10;
			}
			System.out.println(result);
		}

		sc.close();
	}

}
