import java.util.Scanner;
import java.util.ArrayList;

public class B10828 {

	static ArrayList<Integer> stack = new ArrayList<Integer>(0);
	
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // ÃÑ È½¼ö
		
		for(int i = 0; i < n; i++) {
			String s = sc.next();
			
			switch(s) {
			case "push":
				int x = sc.nextInt();
				push(x);
				break;
			case "pop":
				pop();
				break;
			case "size":
				size();
				break;
			case "empty":
				empty();
				break;
			case "top":
				top();
			}
		}
		
		sc.close();
	}
	
	
	static void push(int x) {
		stack.add(x);
	}
	
	static void pop() {
		if(stack.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(stack.get(stack.size() - 1));
			stack.remove(stack.size()-1);
		}
	}

	static void size() {
		System.out.println(stack.size());
	}
	
	static void empty() {
		if(stack.isEmpty()) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}
	}
	
	static void top() {
		if(stack.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(stack.get(stack.size() - 1));
		}
		
	}
	
}
