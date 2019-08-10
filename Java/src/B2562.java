/*
문제
9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
예를 들어, 서로 다른 9개의 자연수
3, 29, 38, 12, 57, 74, 40, 85, 61
이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
입력
첫 째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
출력
첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.
 */
import java.util.Scanner;

public class B2562 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int[] nArray = new int [9]; // 9개의 정수를 받을 배열 생성
		
		for(int i = 0; i < nArray.length; i++) { // 정수 입력 받기
			nArray[i] = sc.nextInt();
		}
		
		int max = nArray[0]; // 최댓값과 그 숫자의 순서로 초기화
		int index = 1;
		
		for(int i = 1; i < nArray.length; i++) { // 최댓값 찾아내고 최댓값이 몇 번째 숫자인지 저장
			if(max < nArray[i]) {
				max = nArray[i];
				index = i + 1;
			}
		}
		
		System.out.println(max); // 출력
		System.out.println(index);
		
		sc.close();
	}

}
