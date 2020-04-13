import java.util.Scanner;

public class B1009 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tCase = sc.nextInt();
		int a, b, c, result;
		
		for(int i = 0; i < tCase; i++) {
			a = sc.nextInt();
			b = sc.nextInt();
			c = 0; // 제곱 수를 줄이기 위한 변수
			result = 1;
			
			if(a % 10 == 0 || a % 10 == 1 || a % 10 == 5 || a % 10 == 6) { // 0, 1, 5, 6 은 마지막 자리 고정
				result = a % 10;
			}else if( a % 10 == 4 || a % 9 == 9) { // 4, 9는 두 번씩 마지막 자리 바뀜
				c = b % 2;
				if(c == 0) {
					c = 2;
				}
			}else { // 나머지는 4번씩 마지막 자리가 바뀜
				c = b % 4;
				if(c == 0) {
					c = 4;
				}
			}
			
			for(int j = 0; j < c; j++) {
				result = (result * a) % 10;
			}
			
			if(result == 0) { // 0이면 10번 컴퓨터가 데이터 처리
				result = 10;
			}
			System.out.println(result);
		}

		sc.close();
	}

}
