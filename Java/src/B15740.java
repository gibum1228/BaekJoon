/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 A와 B (-1010000 ≤ A, B ≤ 1010000)가 주어진다.
출력
첫째 줄에 A+B를 출력한다.
 */
import java.util.Scanner;
import java.math.BigInteger;

public class B15740 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		BigInteger a = sc.nextBigInteger();
		BigInteger b = sc.nextBigInteger();
		
		System.out.println(a.add(b));
		
		sc.close();
	}

}
