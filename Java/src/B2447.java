/*
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
입력
첫째 줄에 N이 주어진다. N은 항상 3의 제곱꼴인 수이다. (3, 9, 27, ...) (N=3k, 1 ≤ k < 8)
출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
 */
import java.util.Arrays;
import java.util.Scanner;

public class B2447 {

	static char[][] board;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long start = System.currentTimeMillis();
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt(); // 3의 제곱줄
		board = new char [size][size];
		
		for(int i = 0; i < size; i++) {
			Arrays.fill(board[i], ' '); // 배열 공백으로 채우기
		}
		
		DrawStar(0, 0, size); // 재귀함수 실행
		
		for(int i = 0; i < size; i++) {
			System.out.println(board[i]); // 2차원 배열 출력
		}
		
		sc.close();
	}

	public static void DrawStar(int x, int y, int size) { // 재귀함수
		if(size == 1) { // * 출력하기
			board[x][y] = '*';
			return;
		}
		
		int divN = size / 3; // 3씩 나누기
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				if(i == 1 && j == 1) { // 공백 남기기
					continue;
				}
				
				DrawStar(x + (i * divN), y + (j * divN), divN);
			}
		}
	}
}
