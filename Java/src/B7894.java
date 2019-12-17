import java.util.Scanner;

public class B7894 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 0; i < n; i++) {
			int m = sc.nextInt();
			double sum = 1.0;
			
			for(int j = m; j > 1; j--) {
				sum += Math.log10(j);
			}
			
			System.out.println((int)sum);
		}
		
		sc.close();
	}
}