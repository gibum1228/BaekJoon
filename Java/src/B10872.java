/*
문제
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 정수 N(0 ≤ N ≤ 12)가 주어진다.
출력
첫째 줄에 N!을 출력한다.
 */
import java.util.Scanner;

public class B10872 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // n! 입력받기
		
		System.out.println(fac(n));
		
		sc.close();
	}
	
	static int fac(int f) { // 팩토리얼 재귀함수
		if(f == 0) { // n이 1이면 1반환
			return 1;
		}else {
			return f * fac(f-1); // f * (f-1)!
		}
	}
}