import java.util.ArrayList;
import java.util.Scanner;

public class B1927 {
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Integer> minHeap = new ArrayList<Integer>();
		minHeap.add(0); // 최소힙 시작을 1부터
		int n = sc.nextInt(); // 연산 횟수
		
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
	
	// 가장 작은 값을 삭제하고 출력하기 위한 메소드
	static void del(ArrayList<Integer> minHeap) {
		
		int lastIndex = minHeap.size() - 1; // 힙의 삭제는 루트 노드와 맨 마지막에 있는 노드를 바꾼 후에, 루트 노드를 기준으르 다시 정렬
		
		System.out.println(minHeap.get(1)); // 가장 작은 값 출력
		minHeap.set(1, minHeap.get(lastIndex)); // 루트 노드를 마지막 요소로 바꿈
		minHeap.remove(lastIndex); // 마지막 요소 삭제
		
		topSort(minHeap); // 루트 노드를 기준으로 정렬
	}
	
	// 최소힙 조건을 맞추기 위한 메소드 (아래에서부터)
	static void underSort(ArrayList<Integer> minHeap) {
		int lastIndex = minHeap.size() - 1;
		
		while(true) {
			if(lastIndex == 1) { // 내가 루트 노드이면
				 break;
			}
			
			int p = minHeap.get(lastIndex / 2); // 부모
			int c = minHeap.get(lastIndex); // 나
			
			if(p < c) { // 부모가 나보다 더 작으면 정렬할 필요가 없음 -> 종료
				break;
			}else {
				int tmp = p; 
				minHeap.set(lastIndex/2, c); // 내가 더 작으니 내가 부모가 되고
				minHeap.set(lastIndex, tmp); // 부모였던 요소가 나의 자식이 됨
				
				lastIndex /= 2; // 내가 부모보다 작지 않을 때까지 무한 반복
			}
		}
	}
	// 위에서부터
	static void topSort(ArrayList<Integer> minHeap) {
		int size = minHeap.size() - 1; // 힙의 크기
		int now = 1; // 현재 루트 노드
		
		while(true) {
			int leftC = now * 2; // 왼쪽 자식 인덱스
			int rightC = now * 2 + 1; // 오른쪽 자식 인덱스
			
			if(leftC > size) { // 자식이 없는 경우 (왼쪽 자식이 없으면 오른쪽 자식도 없는 것임)
				break;
			}else if(rightC <= size) { // 자식 둘 다 있는 경우
				
				if(minHeap.get(leftC) > minHeap.get(now) && minHeap.get(rightC) > minHeap.get(now)) { // 자식이 전부 나보다 크면
					break;
				}else if(minHeap.get(leftC) < minHeap.get(rightC)) { // 왼쪽 자식이 더 작으면
					int tmp = minHeap.get(now);
					minHeap.set(now, minHeap.get(leftC));
					minHeap.set(leftC, tmp);
					
					now = leftC;
				}else { // 오른쪽 자식이 더 작으면
					int tmp = minHeap.get(now);
					minHeap.set(now, minHeap.get(rightC));
					minHeap.set(rightC, tmp);
					
					now = rightC;
				}
				
			}else { // 왼쪽 자식만 있는 경우
				
				if(minHeap.get(leftC) > minHeap.get(now)) { // 자식이 나보다 크면
					break;
				}else { // 아니면 교환
					int tmp = minHeap.get(now);
					minHeap.set(now, minHeap.get(leftC));
					minHeap.set(leftC, tmp);
				}
				
			}
		}
	}
}
