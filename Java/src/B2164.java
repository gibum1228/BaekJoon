import java.util.Scanner;
import java.util.Queue;
import java.util.LinkedList;

public class B2164 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 1 ~ N �Է� �ޱ�
		Queue<Integer> q = new LinkedList<Integer>(); // ť ������ LinkedList�� �ؾ� ��
		
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
