import java.util.Scanner;

public class B9093 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tCase = sc.nextInt();
		sc.nextLine(); // �̰� �� ���� s[1]�� �������� ����  <- nextInt, nextLine ������ �ذ�
		
		for(int i = 0; i < tCase; i++) {
			String s = sc.nextLine();
			String[] sList = s.split(" ");
			
			for(int j = 0; j < sList.length; j++) { // �������� ������ ���� ��ŭ
				
				for(int k = sList[j].length() - 1; k >= 0; k--) { // �������� split�� String ����
					System.out.print(sList[j].charAt(k)); // �ڿ������� ���
				}
				System.out.print(" ");
			}
			System.out.println();
		}
		
		sc.close();
	}

}
