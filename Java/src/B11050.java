import java.util.Scanner;

public class B11050 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // n
		int k = sc.nextInt(); // k
		
		System.out.println(fac(n)/(fac(n-k)*fac(k)));
		
		sc.close();
	}
	
	static int fac(int k) {
		int result = 1;
		
		for(int i = 1; i <= k; i++) {
			result *= i;
		}
		
		return result;
	}

}
