/*
문제
(세 자리 수) × (세 자리 수)는 다음과 같은 과정을 통하여 이루어진다.
(1)과 (2)위치에 들어갈 세 자리 자연수가 주어질 때 (3), (4), (5), (6)위치에 들어갈 값을 구하는 프로그램을 작성하시오.
입력
첫째 줄에 (1)의 위치에 들어갈 세 자리 자연수가, 둘째 줄에 (2)의 위치에 들어갈 세자리 자연수가 주어진다.
출력
첫째 줄부터 넷째 줄까지 차례대로 (3), (4), (5), (6)에 들어갈 값을 출력한다.
 */
import java.util.Scanner;

public class B2588 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int num1 = sc.nextInt(); // (1)
		int num2 = sc.nextInt(); // (2)
		
		int mul1 = num1 * (num2 % 100  % 10); // (3)
		int mul2 = num1 * (num2 % 100 / 10); // (4)
		int mul3 = num1 * (num2 / 100); // (5)
		
		int result = mul1 + (mul2 * 10) + (mul3 * 100); // (6)
		
		System.out.println(mul1);
		System.out.println(mul2);
		System.out.println(mul3);
		System.out.println(result);
		
		sc.close();
	}

}
