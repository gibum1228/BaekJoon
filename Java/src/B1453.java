import java.util.Scanner;

public class B1453 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int count = 0; // �������� ����� ��
		int[] desktop = new int [101]; // 1-100 �¼�
		int n = sc.nextInt(); // �մ��� ��
		
		for(int i = 1; i < desktop.length; i++) {
			desktop[i] = 0; // �� �¼� --> 0
		}
		
		for(int j = 0; j < n; j++) {
			int wantDesk = sc.nextInt();
			
			if(desktop[wantDesk] == 0) { // �� �¼��̸�
				desktop[wantDesk] = 1; // �ڸ� �ִ� �¼� --> 1
			}else {
				count++; // ����� �ִ� �ڸ��� count + 1;
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

}
