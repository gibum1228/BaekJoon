import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class B2164 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 1 ~ N 입력 받기
		Queue<Integer> q = new LinkedList<Integer>(); // 큐 선언은 LinkedList로 해야 됨
		
		for(int i = 1; i <= n; i++) {
			q.offer(i); // push()
		}
		
		while(q.size() != 1) {
			q.poll(); // pop()
			int lastN = q.poll();
			q.offer(lastN);
		}
		
		System.out.println(q.poll());
		
		sc.close();
	}

}
