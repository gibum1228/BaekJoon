import java.util.Scanner;

public class B2480 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int a = sc.nextInt(); // 주사위 눈 입력받기
		int b = sc.nextInt();
		int c = sc.nextInt();
		int result = 0;
		
		if(a == b && a == c) {
			result = 10000 + (a * 1000);
		}else if(a == b || a == c || b == c) {
			if(a == b || a == c) {
				result = 1000 + (a * 100);
			}else {
				result = 1000 + (b * 100);
			}
		}else {
			int max = a;
			if(max < b || max < c) {
				if(b < c) {
					max = c;
				}else {
					max = b;
				}
			}
			
			result = max * 100;
		}
		
		System.out.println(result);
		
		sc.close();
	}

}
