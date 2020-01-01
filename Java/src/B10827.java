import java.math.BigDecimal; // 세밀한 실수 표현 가능
import java.util.Scanner;

public class B10827 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		BigDecimal a = sc.nextBigDecimal(); 
		int b = sc.nextInt();
		
		BigDecimal result = a.pow(b);
		
		System.out.println(result.toPlainString()); // 지수 필드 없이 문자열로 출력
		
		sc.close();
	}

}
