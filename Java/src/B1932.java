import java.util.Scanner;

public class B1932 {

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[][] list = new int[n+1][n+1];
		int sum = 0;

		for (int i = 1; i <= n; i++) {
			for (int j = 1; j <=i; j++) {
				list[i][j] = sc.nextInt();
				if (j == 1) {
					list[i][j] = list[i - 1][j] + list[i][j];
				} else if (i == j) {
					list[i][j] = list[i - 1][j - 1] + list[i][j];
				} else {
					list[i][j] = Math.max(list[i - 1][j], list[i - 1][j - 1]) + list[i][j];
				}

				if (list[i][j] > sum)
					sum = list[i][j];
			}
		}
		
		System.out.println(sum);
		
		sc.close();
	}
}