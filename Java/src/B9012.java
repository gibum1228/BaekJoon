import java.util.Scanner;
import java.util.Stack;

public class B9012 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int nCase = sc.nextInt(); // 케이스
		boolean VPS; // VPS면 true, 아니면 false
		
		for(int i = 0; i < nCase; i++) {
			Stack stack = new Stack(); // 스택
			VPS = true; // default값 VPS
			String s = sc.next(); // () 입력 받기
			
			for(int j = 0; j < s.length(); j++) {
				if(s.charAt(j) == '(') { // '('라면 스택에 저장
					stack.push(s.charAt(j));
				}else if(s.charAt(j) == ')') { // ')'라면
					if(stack.empty() == true) { // 스택이 비어 있을 경우 VPS가 아님
						VPS = false;
						break;
					}else { // 스택이 비어 있지 않다면 '(' pop
						stack.pop();
					}
				}
			}
			
			if(VPS && (stack.size() == 0)) { // VPS이면서 스택에 남아 있는게 없어 크기가 0으로 떨어지면 YES 출력
				System.out.println("YES");
			}else {
				System.out.println("NO");
			}
		}
		
		sc.close();
	}

}
