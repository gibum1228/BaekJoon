import java.util.Scanner;

public class B2775 {
	 public static void main(String[] args) {
	     Scanner sc = new Scanner(System.in);
	     int num = sc.nextInt();
	 
	     for (int i = 0; i < num; i++) {
	         int k = sc.nextInt();
	         int n = sc.nextInt();
	         System.out.println(sum(k, n));
	     }
	     sc.close();
	 }
	 
	 private static int sum(int k, int n) {
		 if (n == 0)
			 return 0;
	     else if (k == 0)
	         return n;
	     else {
	         return sum(k, n - 1) + sum(k - 1, n);
	     }
	 }
}
