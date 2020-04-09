import java.util.Scanner;
import java.math.BigInteger;

public class B2407 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		BigInteger result = BigInteger.ONE;
		
		if(n == m) {
			System.out.println(n);
		}else {
			result = fac(n, m);
			result = result.divide(fac(m, m));
			System.out.println(result);
		}
		
		sc.close();
	}

	static BigInteger fac(long n, int m) {
		BigInteger num = BigInteger.ONE;
		
		for(int i = 0; i < m; i++) {
			num = num.multiply(BigInteger.valueOf(n));
			n--;
		}
		
		return num;
	}
}
