import java.math.BigDecimal; // ������ �Ǽ� ǥ�� ����
import java.util.Scanner;

public class B10827 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		BigDecimal a = sc.nextBigDecimal(); 
		int b = sc.nextInt();
		
		BigDecimal result = a.pow(b);
		
		System.out.println(result.toPlainString()); // ���� �ʵ� ���� ���ڿ��� ���
		
		sc.close();
	}

}
