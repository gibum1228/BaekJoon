import java.util.Scanner;

public class B17496 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // ���� �� ��
		int t = sc.nextInt(); // ���� �ڶ�� �� ��
		int c = sc.nextInt(); // ���� ���� �� �ִ� ĭ ��
		int price = sc.nextInt(); // �� �� �� ����
		
		int result = ((n - 1) / t) * c * price; // �� ����
		
		System.out.println(result);
		
		sc.close();
	}

}
