import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;

public class B10773 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Integer> stack = new ArrayList<Integer>(); // 담을 리스트
		int size = sc.nextInt(); // 반복 횟수
		int result = 0;
		
		for(int i = 0; i < size; i++) {
			int input = sc.nextInt();
			if(input == 0) {
				stack.remove((stack.size() - 1));
			}else {
				stack.add(input);
			}
		}
		
		for(int j = 0; j < stack.size(); j++) {
			result += stack.get(j);
		}
		
		System.out.println(result);
		
		sc.close();
	}

}