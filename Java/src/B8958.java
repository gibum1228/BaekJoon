/*
����
"OOXXOXXOOO"�� ���� OX������ ����� �ִ�. O�� ������ ���� ���̰�, X�� ������ Ʋ�� ���̴�. 
������ ���� ��� �� ������ ������ �� �������� ���ӵ� O�� ������ �ȴ�. ���� ���, 10�� ������ ������ 3�� �ȴ�.
"OOXXOXXOOO"�� ������ 1+2+0+0+1+0+0+1+2+3 = 10���̴�.
OX������ ����� �־����� ��, ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� �׽�Ʈ ���̽��� ������ �־�����. �� �׽�Ʈ ���̽��� �� �ٷ� �̷���� �ְ�, 
���̰� 0���� ũ�� 80���� ���� ���ڿ��� �־�����. ���ڿ��� O�� X������ �̷���� �ִ�.
���
�� �׽�Ʈ ���̽����� ������ ����Ѵ�.
 */
import java.util.Scanner;

public class B8958 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // ���̽� �� �Է¹ޱ�
		char[] oxQuiz;
		
		for(int i = 0; i < n; i++) {
			int count = 0; // ���� ����
			int result = 0; // ����
			String s = sc.next(); // ���ڿ� �Է¹ޱ�
			oxQuiz = s.toCharArray(); // ���������� �ϳ��� �ű��
			
			for(int j = 0; j < oxQuiz.length; j++) { // ������ +, Ʋ���� 0
				if(oxQuiz[j] == 'O') {
					count++;
					result += count;
				}else {
					count = 0;
				}
			}
			
			System.out.println(result); // print
		}

		sc.close();
	}

}
