/*
문제
A+B를 계산하시오.
입력
첫째 줄에 A와 B가 주어진다. (0 < A,B < 1010000)
출력
첫째 줄에 A+B를 출력한다.
 */
import java.math.BigInteger;
import java.util.Scanner;

public class B10757 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		BigInteger a = sc.nextBigInteger();
		BigInteger b = sc.nextBigInteger();
		
		System.out.println(a.add(b));
		
		sc.close();
	}
}
