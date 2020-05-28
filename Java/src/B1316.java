import java.util.Scanner;

public class B1316 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // �׽�Ʈ ���̽�
		int count = 0; // �׷� �ܾ� ����
		
		for(int i = 0; i < n; i++) {
			String s = sc.next();
			if(checkWord(s)) { // �׷� �ܾ� üĿ
				count++;
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

	public static boolean checkWord(String s) {
		
		boolean[] alphabet = new boolean [26]; // ���ӵ��� �ʴ� �ߺ��� �ܾ �ִ��� �Ǵ��ϱ� ���� �迭
		
		for(int i = 0; i < s.length(); i++) {
			char text = s.charAt(i); // i��° �ܾ� üũ
			
			if(alphabet[text - 'a']) { // �̹� üũ�� ���ĺ��̸� false ����
				return false;
			}else {
				if(i < s.length()-1 && text != s.charAt(i+1)) { // i��° �ش��ϴ� ���ĺ��� ������ ������ ������ true �ֱ�
					alphabet[text - 'a'] = true;
				}
			}
		}
		
		return true; // ���������� �ߺ��� �ܾ ���� ��� true ����
	}
}
