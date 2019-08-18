/*
++++++++++++ 에라토스테네스의 체
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
 */
import java.util.Scanner;

public class B1929 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int minN = sc.nextInt(); // 최소
		int maxN = sc.nextInt(); // 최대
		int[] digitList = new int [maxN+1]; // maxN까지의 배열
		
		for(int i = 2; i < digitList.length; i++) { // 2부터 배열 길이까지 숫자 넣기
			digitList[i] = i;
		}
		
		for(int i = 2; i< digitList.length; i++) {  // 배수에 0넣기
			if(digitList[i] == 0) {  // i의 배수가 이미 0이면 스킵
				continue;
			}
			for(int j = i+i; j < digitList.length; j += i) { // 배수인 인덱스에 0 넣기
					digitList[j] = 0;
			}
		}
		
		for(int i = minN; i < digitList.length; i++) { // 소수인 인덱스 출력
			if(digitList[i] != 0) {
				System.out.println(digitList[i]);
			}
		}
		
		sc.close();
	}

}
