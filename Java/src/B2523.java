import java.util.Scanner;

public class B2523 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 횟수
		
		for(int i = 1; i <= n; i++) { // 상단
			for(int j = 0; j < i; j++) {
				System.out.print("*");
			}
			System.out.println();
		}

		for(int i = n-1; i > 0; i--) { // 하단
			for(int j = i; j > 0; j--) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		sc.close();
	}

}
