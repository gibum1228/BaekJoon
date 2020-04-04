import java.util.Scanner;
import java.util.ArrayList;

public class B10845 {

	static ArrayList<Integer> queue = new ArrayList<Integer>(0);
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt();
		
		for(int i = 0; i < size; i++) {
			String op = sc.next();
			
			switch(op) {
			case "push":
				int n = sc.nextInt();
				push(n);
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
			case "front":
				front();
				break;
			case "back":
				back();
			}
		}
		
		sc.close();
	}
	
	static void push(int n) {
		queue.add(n);
	}
	static void pop() {
		if(queue.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(queue.get(0));
			queue.remove(0);
		}
	}
	static void size() {
		System.out.println(queue.size());
	}
	static void empty() {
		if(queue.isEmpty()) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}
	}
	static void front() {
		if(queue.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(queue.get(0));
		}
	}
	static void back() {
		if(queue.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(queue.get(queue.size()-1));
		}
	}

}
