import java.util.Scanner;

public class B2443 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 높이
		
		for(int i = 0; i < n; i++) { // 밑변이 위에 있어 아래로 뻗는 삼각형 출력
			for(int j = 0; j < i; j++) {
				System.out.print(" ");
			}
			for(int k = 0; k < 2*n - 1 - i*2; k++) { // 2n - 1, 2n - 3, 2n - 5, ... 개를 출력
				System.out.print("*");
			}
			System.out.println();
		}
		
		sc.close();
	}

}
