import java.util.Scanner;

public class B2702 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tCase = sc.nextInt();
		
		for(int i = 0; i < tCase; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			System.out.println(lcm(a, b) + " " + gcd(a, b)); // '�ּҰ���� �ִ�����' ���
		}
		
		sc.close();
	}

	public static int gcd(int a, int b) { // ��Ŭ���� ȣ����(�ִ� �����)
		int r;
		
		while(b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		
		return a;
	}
	
	public static int lcm(int a, int b) { // ��Ŭ���� ȣ�������� �ּ� ����� ���ϱ�
		return (a * b) / gcd(a, b);
	}
}
