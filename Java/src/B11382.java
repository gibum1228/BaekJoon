import java.util.Scanner;
import java.math.BigInteger;

public class B11382 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		BigInteger a = sc.nextBigInteger();
		BigInteger b = sc.nextBigInteger();
		BigInteger c = sc.nextBigInteger();
	
		BigInteger result = a.add(b.add(c));
		
		System.out.println(result);
		
		sc.close();
	}

}
