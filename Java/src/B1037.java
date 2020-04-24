import java.util.Arrays;
import java.util.Scanner;

public class B1037 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] intList = new int [n];
		
		for(int i = 0; i < n; i++) {
			intList[i] = sc.nextInt();
		}
		
		if(n == 1) {
			System.out.println(intList[0] * intList[0]);
		}else {
			Arrays.sort(intList);
			System.out.println(intList[0] * intList[n-1]);
		}
		
		sc.close();
	}

}
