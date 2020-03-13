import java.util.Scanner;
import java.math.BigInteger;

public class B10826 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		BigInteger f0 = BigInteger.ZERO;
		BigInteger f1 = BigInteger.ONE;
		BigInteger fn = BigInteger.ZERO;
		
		if(n == 0) {
			System.out.println(0);
		}else if(n == 1) {
			System.out.println(1);
		}else {
			for(int i = 0; i < n-1; i++) {
				fn = f0.add(f1);
				f0 = f1;
				f1 = fn;
			}
			
			System.out.println(fn);
		}
		
		sc.close();
	}

}
