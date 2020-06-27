import java.util.Scanner;
import java.util.Stack;

public class B9012 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int nCase = sc.nextInt(); // ���̽�
		boolean VPS; // VPS�� true, �ƴϸ� false
		
		for(int i = 0; i < nCase; i++) {
			Stack stack = new Stack(); // ����
			VPS = true; // default�� VPS
			String s = sc.next(); // () �Է� �ޱ�
			
			for(int j = 0; j < s.length(); j++) {
				if(s.charAt(j) == '(') { // '('��� ���ÿ� ����
					stack.push(s.charAt(j));
				}else if(s.charAt(j) == ')') { // ')'���
					if(stack.empty() == true) { // ������ ��� ���� ��� VPS�� �ƴ�
						VPS = false;
						break;
					}else { // ������ ��� ���� �ʴٸ� '(' pop
						stack.pop();
					}
				}
			}
			
			if(VPS && (stack.size() == 0)) { // VPS�̸鼭 ���ÿ� ���� �ִ°� ���� ũ�Ⱑ 0���� �������� YES ���
				System.out.println("YES");
			}else {
				System.out.println("NO");
			}
		}
		
		sc.close();
	}

}
