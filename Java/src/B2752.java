import java.util.Arrays;
import java.util.Scanner;

public class B2752 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] intList = new int [3];
		
		for(int i = 0; i < intList.length; i++) {
			intList[i] = sc.nextInt();
		}
		
		Arrays.sort(intList);
		
		System.out.println(intList[0] + " " + intList[1] + " " + intList[2]);
		
		sc.close();
	}

}
