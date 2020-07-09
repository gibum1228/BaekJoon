import java.util.Scanner;

public class B14490 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String[] s = sc.next().split(":");
		int a = Integer.parseInt(s[0]);
		int b = Integer.parseInt(s[1]);
		
		int gcdN = gcd(a, b);
		
		System.out.println(a/gcdN + ":" + b/gcdN);
		
		sc.close();
	}

	static int gcd(int a, int b) {
		int r;
		
		while(b != 0) {
			r = a % b;
			a = b;
			b = r;
		}
		
		return a;
	}
}
