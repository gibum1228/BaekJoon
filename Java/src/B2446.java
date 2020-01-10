import java.util.Scanner;

public class B2446 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		
		for(int i = 0; i < (2 * n) / 2; i++) { // 윗부분 출력
			for(int j = 0; j < i; j++) {
				System.out.print(" ");
			}
			for(int k = i + i; k < (2 * n - 1); k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		for(int i = 1; i <= (2 * n - 1) / 2; i++) { // 아랫부분 출력
			for(int j = i; j < (2* n - 1) / 2; j++) {
				System.out.print(" ");
			}
			for(int k = 0; k <= i + i; k++) {
				System.out.print("*");
			}
			System.out.println();
		}
		
		sc.close();
	}

}
