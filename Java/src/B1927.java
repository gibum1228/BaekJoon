import java.util.ArrayList;
import java.util.Scanner;

public class B1927 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Integer> minHeap = new ArrayList<Integer>();
		minHeap.add(0); // �ּ��� ������ 1����
		int n = sc.nextInt(); // ���� Ƚ��
		
		for(int i = 1; i <= n; i++) {
			int x = sc.nextInt();
			
			if(x == 0) {
				if((minHeap.size() - 1) == 0) {
					System.out.println("0");
				}else {
					del(minHeap);
				}
			}else {
				minHeap.add(x);
				underSort(minHeap);
			}
		}
		
		sc.close();
	}
	
	// ���� ���� ���� �����ϰ� ����ϱ� ���� �޼ҵ�
	static void del(ArrayList<Integer> minHeap) {
		
		int lastIndex = minHeap.size() - 1; // ���� ������ ��Ʈ ���� �� �������� �ִ� ��带 �ٲ� �Ŀ�, ��Ʈ ��带 �������� �ٽ� ����
		
		System.out.println(minHeap.get(1)); // ���� ���� �� ���
		minHeap.set(1, minHeap.get(lastIndex)); // ��Ʈ ��带 ������ ��ҷ� �ٲ�
		minHeap.remove(lastIndex); // ������ ��� ����
		
		topSort(minHeap); // ��Ʈ ��带 �������� ����
	}
	
	// �ּ��� ������ ���߱� ���� �޼ҵ� (�Ʒ���������)
	static void underSort(ArrayList<Integer> minHeap) {
		int lastIndex = minHeap.size() - 1;
		
		while(true) {
			if(lastIndex == 1) { // ���� ��Ʈ ����̸�
				 break;
			}
			
			int p = minHeap.get(lastIndex / 2); // �θ�
			int c = minHeap.get(lastIndex); // ��
			
			if(p < c) { // �θ� ������ �� ������ ������ �ʿ䰡 ���� -> ����
				break;
			}else {
				int tmp = p; 
				minHeap.set(lastIndex/2, c); // ���� �� ������ ���� �θ� �ǰ�
				minHeap.set(lastIndex, tmp); // �θ𿴴� ��Ұ� ���� �ڽ��� ��
				
				lastIndex /= 2; // ���� �θ𺸴� ���� ���� ������ ���� �ݺ�
			}
		}
	}
	// ����������
	static void topSort(ArrayList<Integer> minHeap) {
		int size = minHeap.size() - 1; // ���� ũ��
		int now = 1; // ���� ��Ʈ ���
		
		while(true) {
			int leftC = now * 2; // ���� �ڽ� �ε���
			int rightC = now * 2 + 1; // ������ �ڽ� �ε���
			
			if(leftC > size) { // �ڽ��� ���� ��� (���� �ڽ��� ������ ������ �ڽĵ� ���� ����)
				break;
			}else if(rightC <= size) { // �ڽ� �� �� �ִ� ���
				
				if(minHeap.get(leftC) > minHeap.get(now) && minHeap.get(rightC) > minHeap.get(now)) { // �ڽ��� ���� ������ ũ��
					break;
				}else if(minHeap.get(leftC) < minHeap.get(rightC)) { // ���� �ڽ��� �� ������
					int tmp = minHeap.get(now);
					minHeap.set(now, minHeap.get(leftC));
					minHeap.set(leftC, tmp);
					
					now = leftC;
				}else { // ������ �ڽ��� �� ������
					int tmp = minHeap.get(now);
					minHeap.set(now, minHeap.get(rightC));
					minHeap.set(rightC, tmp);
					
					now = rightC;
				}
				
			}else { // ���� �ڽĸ� �ִ� ���
				
				if(minHeap.get(leftC) > minHeap.get(now)) { // �ڽ��� ������ ũ��
					break;
				}else { // �ƴϸ� ��ȯ
					int tmp = minHeap.get(now);
					minHeap.set(now, minHeap.get(leftC));
					minHeap.set(leftC, tmp);
				}
				
			}
		}
	}
}
