/*
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다. 
점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
 */
import java.util.Scanner;

public class B4344 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		// 평균을 넘는 학생들의 비율은 avgUpCount / studentCount * 100
		int sum; // 성적 총합
		int avg; // 평균
		double avgUpCount; // 평균 넘는 학생 수
		int classCount = sc.nextInt(); // 학급 개수
		int[][] gradeArray = new int [classCount][1000]; // 학급 별 2차원 배열
		
		for(int i = 0; i < classCount; i++) {
			sum = 0; // 초기화
			avg = 0;
			avgUpCount = 0;
			int studentCount = sc.nextInt(); // 학급 인원 수
			
			for(int j = 0; j < studentCount; j++) { // 학급 인원 수대로 점수 채우기
				gradeArray[i][j] = sc.nextInt();
			}
			
			for(int k = 0; k < studentCount; k++) { // 총합 구하기
				sum += gradeArray[i][k];
			}
			
			avg = sum / studentCount; // 평균 구하기
			
			for(int l = 0; l < studentCount; l++) { // 평균이 넘는 학생 수 구하기
				if(gradeArray[i][l] > avg) {
					avgUpCount++;
				}
			}
			
			double answer = (avgUpCount / (double)studentCount) * 100.0; // 비율 구하기
			
			System.out.printf("%.3f%%\n", answer); // print
		}
		
		sc.close();
	}

}
