import java.util.Scanner;

public class B2609 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int m = sc.nextInt();
		
		System.out.println(gcd(n, m));
		System.out.println(lcm(n, m));
		
		sc.close();
	}

	static int gcd(int a, int b) { // �ִ� ����� (��Ŭ������ ȣ����
		int r;
		
		while(b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		
		return a;
	}
	
	static int lcm(int a, int b) { // �ּ� �����
		return (a * b) / gcd(a, b);
	}
}
