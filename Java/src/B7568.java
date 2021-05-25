import java.util.Scanner;

public class B7568 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // n만큼 작동
		int[][] weight = new int [n][2]; // 덩치 저장
		int[] rank = new int [n];
		
		for(int i = 0; i < n; i++) { // 덩치 구하기
			int kg = sc.nextInt();
			int height = sc.nextInt();
			
			// input
			weight[i][0] = kg;
			weight[i][1] = height;
			rank[i] = 1; // 초기화
		}
		
		for(int i = 0; i < n; i++) { // 브루트포스 알고리즘
			
			for(int j = 0; j < n; j++) {
				
				if(i == j) { // 자기 자신과 비교 불가능
					continue;
				}
				// 키와 몸무게가 모두 커야 덩치가 큰 것임
				if(weight[i][0] < weight[j][0] && weight[i][1] < weight[j][1]) { // 덩치가 작으면 순위 밀림
					rank[i]++;
				}
			}
		}
		
		for(int i = 0; i < n; i++) {
			System.out.print(rank[i] + " ");
		}
		
		sc.close();
	}

}