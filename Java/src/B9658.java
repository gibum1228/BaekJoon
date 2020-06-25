import java.util.Scanner;

public class B9658 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] dpNum = new int [1001];
		
		int n = sc.nextInt();
		
		dpNum[1] = 0;
		dpNum[2] = 1; // 1-1
		dpNum[3] = 0;
		dpNum[4] = 1; // 3-1
		
		for(int i = 5; i <= 1000; i++) {
			if(dpNum[i - 1] + dpNum[i - 3] + dpNum[i - 4] < 3) {
				dpNum[i] = 1;
			}else {
				dpNum[i] = 0;
			}
		}
		
		if(dpNum[n] == 1) {
			System.out.println("SK");
		}else {
			System.out.println("CY");
		}
		
		sc.close();
	}
}
