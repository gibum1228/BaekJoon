/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력
첫째 줄에 A+B를 출력한다.
 */
import java.util.Scanner;

public class B1000 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
			Scanner sc = new Scanner(System.in);
			
			int A = sc.nextInt();
			int B = sc.nextInt();
			
			System.out.print(A+B);
			sc.close();
	}

}
