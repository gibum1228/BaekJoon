import java.util.Scanner;
import java.util.Stack;

public class B4949 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) { // 연산 수행
			Stack<Character> stack = new Stack<>(); // 괄호 판단할 스택
			String s = sc.nextLine(); // 한 문장
			boolean result = true; // 균형, 불균형 판단
			
			if(s.compareTo(".") == 0) { // .만 입력할 경우 프로그램 종료
				break;
			}
			
			for(int i = 0; i < s.length(); i++) {
				if(s.charAt(i) == '(' || s.charAt(i) == '[') { // 왼쪽 괄호이면 스택에 푸쉬
					stack.push(s.charAt(i));
					
				}else if(s.charAt(i) == ')') { // 오른쪽 소괄호일 때
					if(stack.empty() || stack.pop() != '(') { // 스택이 비어있거나 맞는 짝이 없으면 불균형
						result = false;
						break;
					}
					
				}else if(s.charAt(i) == ']') { // 오른쪽 대괄호일 때
					if(stack.empty() || stack.pop() != '[') { // 스택이 비어있거나 맞는 짝이 없으면 불균형
						result = false;
						break;
					}
				}
			}
			
			if(!(stack.empty())) { // 스택에 ( 또는 [가 있는 경우 불균형
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
