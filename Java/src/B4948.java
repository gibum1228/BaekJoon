/*
문제
베르트랑 공준은 임의의 자연수 n에 대하여, n보다 크고, 2n보다 작거나 같은 소수는 적어도 하나 존재한다는 내용을 담고 있다.
이 명제는 조제프 베르트랑이 1845년에 추측했고, 파프누티 체비쇼프가 1850년에 증명했다.
예를 들어, 10보다 크고, 20보다 작거나 같은 소수는 4개가 있다. 
(11, 13, 17, 19) 또, 14보다 크고, 28보다 작거나 같은 소수는 3개가 있다. (17,19, 23)
n이 주어졌을 때, n보다 크고, 2n보다 작거나 같은 소수의 개수를 구하는 프로그램을 작성하시오. 
입력
입력은 여러 개의 테스트 케이스로 이루어져 있다. 각 케이스는 n을 포함하며, 한 줄로 이루어져 있다. (n ≤ 123456)
입력의 마지막에는 0이 주어진다.
출력
각 테스트 케이스에 대해서, n보다 크고, 2n보다 작거나 같은 소수의 개수를 출력한다.
 */
import java.util.*;

public class B4948 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		
		while(true) {
			int minN = sc.nextInt(); // 최소
			if(minN == 0) {
				break;
			}
			int maxN = 2 * minN; // 최대
			int[] digitList = new int [maxN+1]; // maxN까지의 배열
			int count = 0; // 소수 갯수 셀 변수
			
			for(int i = 2; i < digitList.length; i++) { // 2부터 배열 길이까지 숫자 넣기
				digitList[i] = i;
			}
			
			for(int i = 2; i < digitList.length; i++) {  // 배수에 0넣기
				if(digitList[i] == 0) {  // i의 배수가 이미 0이면 스킵
					continue;
				}
				for(int j = i+i; j < digitList.length; j += i) { // 배수인 인덱스에 0 넣기
						digitList[j] = 0;
				}
			}
			
			for(int i = minN + 1; i < digitList.length; i++) { // 소수 갯수 세기 < minN보다 크고 maxN보다 작거나 같은 >
				if(digitList[i] != 0) {
					count++;
				}
			}
			
			System.out.println(count);
		}
		
		sc.close();
	}

}
