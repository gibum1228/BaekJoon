import java.util.Scanner;
import java.util.Stack;

public class B4949 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) { // ���� ����
			Stack<Character> stack = new Stack<>(); // ��ȣ �Ǵ��� ����
			String s = sc.nextLine(); // �� ����
			boolean result = true; // ����, �ұ��� �Ǵ�
			
			if(s.compareTo(".") == 0) { // .�� �Է��� ��� ���α׷� ����
				break;
			}
			
			for(int i = 0; i < s.length(); i++) {
				if(s.charAt(i) == '(' || s.charAt(i) == '[') { // ���� ��ȣ�̸� ���ÿ� Ǫ��
					stack.push(s.charAt(i));
					
				}else if(s.charAt(i) == ')') { // ������ �Ұ�ȣ�� ��
					if(stack.empty() || stack.pop() != '(') { // ������ ����ְų� �´� ¦�� ������ �ұ���
						result = false;
						break;
					}
					
				}else if(s.charAt(i) == ']') { // ������ ���ȣ�� ��
					if(stack.empty() || stack.pop() != '[') { // ������ ����ְų� �´� ¦�� ������ �ұ���
						result = false;
						break;
					}
				}
			}
			
			if(!(stack.empty())) { // ���ÿ� ( �Ǵ� [�� �ִ� ��� �ұ���
				result = false;
			}
			
			if(result) {
				System.out.println("yes");
			}else {
				System.out.println("no");
			}
		}

		sc.close();
	}
}
