import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class B1026 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] a = new int [n];
		Integer[] b = new Integer [n];
		int result = 0;
		
		for(int i = 0; i < n; i++) {
			a[i] = sc.nextInt();
		}
		for(int i = 0; i < n; i++) {
			b[i] = sc.nextInt();
		}
		Integer[] bCopy = b;
		
		Arrays.sort(a);
		Arrays.sort(bCopy, Collections.reverseOrder());
		
		for(int i = 0; i < n; i++) {
			result += a[i] * bCopy[i];
		}
		
		System.out.println(result);
		
		sc.close();
	}
}
