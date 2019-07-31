/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력
각 테스트 케이스마다 A+B를 출력한다.
 */
import java.util.Scanner;

public class B10950 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int[] ab = new int[2];
		int size = sc.nextInt();
		
		for(int i = 0; i < size; i++) {
			int a = sc.nextInt();
			int b = sc.nextInt();
			
			ab[0] = a;
			ab[1] = b;
			
			System.out.println(a + b);
		}
		
		sc.close();
	}

}
