import java.util.Scanner;
import java.util.ArrayList;

public class B11866 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 1~n의 정수 
		int k = sc.nextInt(); // jump 수
		int[] oneToN = new int [n+1]; // 1~n을 저장하는 배열
		ArrayList<Integer> sequence = new ArrayList<Integer>(); // 요세푸스 수열

		for(int i = 0; i < n+1; i++) { // 1~n 생성
			oneToN[i] = i;
		}
		
		int index = 1; // index 시작점 1
		for(int a = 1; a <= n; a++) { // n만큼
			
			int b = 0; // k번 판단할 변수
			while(true) {
				if(b == k) { // k만큼 비교했으면 while 종료 
					break;
				}
				
				if(oneToN[index] == -1) { // 이미 들린 숫자면
					index++; // 숫자 세지 말고 다음 칸으로 넘어가기
					if(index > n) {
						index %= n;
					}
					continue;
				}
				
				if(b == k-1) { // 0~k-1이 k번만큼 움직인 것임.
					sequence.add(oneToN[index]); // 수열에 값을 넣고
					
					oneToN[index] = -1; // index 값 -1로 지정해 이미 들린 인덱스라는 걸 표시
				}
				
				index++; // 다음 인덱스로 가기
				if(index > n) { // index 오버 방지
					index %= n;
				}

				b++;
			}
		}
		
		System.out.print("<"); // print
		for(int i = 0; i < sequence.size(); i++) {
			if(i == sequence.size()-1) {
				System.out.println(sequence.get(i) + ">");
			}else {
				System.out.print(sequence.get(i) + ", ");
			}
		}
		
		sc.close();
	}

}
