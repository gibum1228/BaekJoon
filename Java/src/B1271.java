import java.math.BigInteger;
import java.util.Scanner;

public class B1271 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		BigInteger n = sc.nextBigInteger(); // 최백준이 받는 돈
		BigInteger m = sc.nextBigInteger(); // 나눠 가질 사람 수
		
		System.out.println(n.divide(m)); // 나눠 가질 수 있는 돈
		System.out.println(n.remainder(m)); // 남는 돈
 		
		sc.close();
	}

}
