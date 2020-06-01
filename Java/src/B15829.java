import java.util.Scanner;

public class B15829 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // ���̽� Ƚ��
		String s = sc.next(); // ���ڿ� �Է¹ޱ�
		final Long MOD = 1234567891L; // M�� ����
		Long temp = 1L; // r�� i ���� ��
		Long result = 0L;
		
		for(int i = 0; i < n; i++) {
			int c = (s.charAt(i) - 'a' + 1) * 1; // �ؽð�
			
			result += c * temp % MOD; 
			temp *= 31; // r�� i����
			temp %= MOD;
		}
		
		System.out.println(result % MOD);
		
		sc.close();
	}

}
