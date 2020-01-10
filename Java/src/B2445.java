import java.util.Scanner;

public class B2445 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 1; i <= 2 * n / 2; i++) { // 윗부분 출력
			for(int j = 0; j < i; j++) {
				System.out.print("*");
			}
			for(int k = 0; k < 2 * n - i - i; k++) {
				System.out.print(" ");
			}
			for(int l = 0; l < i; l++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i = 1; i <= (2 * n - 1) / 2; i++) { // 아랫부분 출력
			for(int j = i; j <= (2 * n - 1) / 2; j++) {
				System.out.print("*");
			}
			for(int k = 0; k < i + i; k++) {
				System.out.print(" ");
			}
			for(int l = i; l <= (2 * n - 1) / 2; l++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		sc.close();
	}

}
