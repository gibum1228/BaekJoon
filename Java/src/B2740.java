import java.util.Scanner;

public class B2740 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int m = sc.nextInt();
		int[][] aList = new int [n][m];
		for(int i = 0; i < n; i++) { // a �迭 �Է� �ޱ�
			for(int j = 0; j < m; j++) {
				aList[i][j] = sc.nextInt();
			}
		}
		
		m = sc.nextInt();
		int k = sc.nextInt();
		int[][] bList = new int [m][k];
		for(int i = 0; i < m; i++) { // b �迭 �Է� �ޱ�
			for(int j = 0; j < k; j++) {
				bList[i][j] = sc.nextInt();
			}
		}
		
		for(int i = 0; i < n; i++) { // a �� ��ŭ
			for(int j = 0; j < k; j++) { // b �� ��ŭ
				int result = 0;
				for(int l = 0; l < m; l++) { // ��� ����
					result += aList[i][l] * bList[l][j];
				}
				
				System.out.print(result + " ");
			}
			System.out.println("");
		}
		
		sc.close();
	}

}
