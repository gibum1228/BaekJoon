/*
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.
입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.
출력
직사각형의 네 번째 점의 좌표를 출력한다.
 */
import java.util.Scanner;

public class B3009 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int x1 = sc.nextInt(); // 좌표 입력받기
		int y1 = sc.nextInt();
		int x2 = sc.nextInt();
		int y2 = sc.nextInt();
		int x3 = sc.nextInt();
		int y3 = sc.nextInt();
		int x4 = 0;
		int y4 = 0;
		
		// 네번째 점의 x 좌표 구하기
		if(x1 == x2) {
			x4 = x3;
		}
		if(x2 == x3) {
			x4 = x1;
		}
		if(x1 == x3) {
			x4 = x2;
		}
		
		// 네번째 점의 y 좌표 구하기
		if(y1 == y2) {
			y4 = y3;
		}
		if(y2 == y3) {
			y4 = y1;
		}
		if(y1 == y3) {
			y4 = y2;
		}
		
		System.out.println(x4 + " " + y4); // 출력
		
		sc.close();
	}

}
