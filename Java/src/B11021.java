/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
 */
import java.util.Scanner;

public class B11021 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int t = sc.nextInt(); // 테스트 케이스 크기인 t 입력받기
		
		for(int i = 1; i <= t; i++) { // t만큼 반복
			int a = sc.nextInt(); // a, b 입력받기
			int b= sc.nextInt();
			
			System.out.println("Case #" + i + ": " + (a+b)); // i로 케이스 번호 표현해 a+b를 출력
		}
		
		sc.close();
	}

}
