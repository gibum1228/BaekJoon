import java.util.Scanner;

public class B2702 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int tCase = sc.nextInt();
		
		for(int i = 0; i < tCase; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			System.out.println(lcm(a, b) + " " + gcd(a, b)); // '최소공배수 최대공약수' 출력
		}
		
		sc.close();
	}

	public static int gcd(int a, int b) { // 유클리드 호제법(최대 공약수)
		int r;
		
		while(b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		
		return a;
	}
	
	public static int lcm(int a, int b) { // 유클리드 호제법으로 최소 공배수 구하기
		return (a * b) / gcd(a, b);
	}
}
