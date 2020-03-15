import java.util.Scanner;

public class B1564 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long n = sc.nextInt();
		String s = "1";
		long result;
		int countZero; // 0의 개수 구하는 변수
		
		for(int i = 2; i <= n; i++) {
			result = Long.parseUnsignedLong(s) * i; // 팩토리얼 값 구하기
			s = Long.toString(result); // 팩토리얼 값 문자열로 만들기
			countZero = 0; // 0의 갯수 구하는 변수 초기화
			
			for(int j = s.length() - 1; j >= 0; j--) {
				if(s.charAt(j) == '0'){ // 뒤에 연속된 0의 개수 구하기
					countZero++;
					continue;
				}
				
				s = s.substring(0, s.length() - countZero); // 처음부터 뒤에서 0이 없는 시점까지 자르기
				break;
			}
		
			if(s.length() > 12) { // Long 범위
				s = s.substring(s.length() - 12);
			}
		}
		
		if(s.length() > 5) {
			s = s.substring(s.length() - 5, s.length());
		}
		
		System.out.println(s); // 출력
		
		sc.close();
	}
}
