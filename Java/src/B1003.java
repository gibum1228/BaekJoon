import java.util.Scanner;

public class B1003 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // TestCase
		int[][] f = new int [41][2]; // n은 최대 40, 동적 프로그래밍
		f[0][0] = 1;
		f[1][1] = 1;
		
		for(int i = 2; i < 41; i++) {
			for(int j = 0; j < 2; j++) {
				f[i][j] = f[i-1][j] + f[i-2][j]; // 0과 1의 갯수는 (n-1) + (n-2)와 같다.
			}
		}
		
		for(int i = 0; i < n; i++) {
			int a = sc.nextInt();
			System.out.println(f[a][0] + " " + f[a][1]);
		}
		
		sc.close();
	}
}
