import java.util.Scanner;

public class B3003 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int[] chess = {1, 1, 2, 2, 2, 8};
		int[] inputCount = new int [6];
		
		for(int i = 0; i < 6; i++) {
			int n = sc.nextInt();
			
			inputCount[i] = n;
		}
		
		for(int j = 0; j < 6; j++) {
			chess[j] = chess[j] - inputCount[j];
		}
		
		for(int k = 0; k < 6; k++) {
			System.out.print(chess[k] + " ");
		}
		
		sc.close();
	}

}
