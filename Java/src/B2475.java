import java.util.Scanner;

public class B2475 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int result = 0;
		
		for(int i = 0; i < 5; i++) {
			int n = sc.nextInt();
			
			result += (n * n);
		}
		
		System.out.println(result % 10);
		
		sc.close();
	}

}
