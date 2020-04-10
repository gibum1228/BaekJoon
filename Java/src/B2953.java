import java.util.Scanner;

public class B2953 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] sumList = new int [6];
		
		int sum;
		
		for(int i = 1; i < 6; i++) {
			sum = 0;
			
			for(int j = 0; j < 4; j++) {
				int n = sc.nextInt();
				
				sum += n;
			}
			
			sumList[i] = sum;
		}
		
		int max = 1;
		for(int k = 2; k < 6; k++) {
			if(sumList[max] < sumList[k]) {
				max = k;
			}
		}
		
		System.out.println(max + " " + sumList[max]);
		
		sc.close();
	}

}
