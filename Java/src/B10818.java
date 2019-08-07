/*
문제
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
입력
첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
출력
첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
 */
import java.util.Scanner;

public class B10818 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt(); // 입력받을 정수 갯수
		
		int[] num = new int [size]; // size 크기의 배열 생성
		
		for(int i = 0; i < size; i++) { // 정수 입력 받기
			num[i] = sc.nextInt();
		}
		
		int min = num[0]; // 최소값 num[0]으로 초기화
		int max = num[0]; // 최댓값 num[0]으로 초기화
		
		for(int i = 1; i < size; i++) { // 인덱스 1번부터 끝까지 비교하여 배열의 최소값과 최댓값 찾기
			if(min > num[i]) {
				min = num[i];
			}
			if(max < num[i]) {
				max = num[i];
			}
		}
		
		System.out.println(min + " " + max); // 출력하기
		
		sc.close();
	}

}
