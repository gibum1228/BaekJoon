import java.util.Arrays;
import java.util.Scanner;

public class B11399 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int size = sc.nextInt();
		int[] customer = new int [size];
		int result = 0;
		
		for(int i = 0; i < size; i++) {
			customer[i] = sc.nextInt();
		}
		
		Arrays.sort(customer);
		
		for(int i = 0; i < size; i++) {
			for(int j = 0; j <= i; j++) {
				result += customer[j];
			}
		}
		
		System.out.println(result);
		
		sc.close();
	}

}
