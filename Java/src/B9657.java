import java.util.Scanner;

public class B9657 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] dpNum = new int [10001];
		
		int n = sc.nextInt();
		
		dpNum[1] = 1;
		dpNum[2] = 0;
		dpNum[3] = 1;
		dpNum[4] = 1;
		
		for(int i = 5; i <= 1000; i++) {
			if((dpNum[i-1] + dpNum[i-3] + dpNum[i-4]) == 3) {
				dpNum[i] = 0;
			}else {
				dpNum[i] = 1;
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
