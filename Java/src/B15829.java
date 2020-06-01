import java.util.Scanner;

public class B15829 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 케이스 횟수
		String s = sc.next(); // 문자열 입력받기
		final Long MOD = 1234567891L; // M을 지정
		Long temp = 1L; // r의 i 제곱 값
		Long result = 0L;
		
		for(int i = 0; i < n; i++) {
			int c = (s.charAt(i) - 'a' + 1) * 1; // 해시값
			
			result += c * temp % MOD; 
			temp *= 31; // r의 i제곱
			temp %= MOD;
		}
		
		System.out.println(result % MOD);
		
		sc.close();
	}

}
