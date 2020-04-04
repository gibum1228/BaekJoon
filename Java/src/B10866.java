import java.util.ArrayList;
import java.util.Scanner;

public class B10866 {

	static ArrayList<Integer> deque = new ArrayList<Integer>(0);
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int size = sc.nextInt();
		for(int i = 0; i < size; i++) {
			String op = sc.next();
			
			switch(op) {
			case "push_front":
				int n1 = sc.nextInt();
				push_front(n1);
				break;
			case "push_back":
				int n2 = sc.nextInt();
				push_back(n2);
				break;
			case "pop_front":
				pop_front();
				break;
			case "pop_back":
				pop_back();
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
	
	static void push_front(int n) {
		deque.add(0, n);
	}
	static void push_back(int n) {
		deque.add(deque.size(), n);
	}
	static void pop_front() {
		if(deque.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(deque.get(0));
			deque.remove(0);
		}
	}
	static void pop_back() {
		if(deque.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(deque.get(deque.size() - 1));
			deque.remove(deque.size()-1);
		}
	}
	static void size() {
		System.out.println(deque.size());
	}
	static void empty() {
		if(deque.isEmpty()) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}
	}
	static void front() {
		if(deque.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(deque.get(0));
		}
	}
	static void back() {
		if(deque.isEmpty()) {
			System.out.println(-1);
		}else {
			System.out.println(deque.get(deque.size()-1));
		}
	}
	
}
