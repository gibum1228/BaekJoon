/*
A+B - 4
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	36716	13785	11795	39.719%
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력
입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력
각 테스트 케이스마다 A+B를 출력한다.
 */
import java.util.Scanner;

public class B10951 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while(sc.hasNextInt()) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			System.out.println(a+b);
		}
		
		sc.close();
	}

}
