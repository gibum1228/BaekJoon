import java.util.Scanner;

public class B1453 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int count = 0; // 거절당한 사람의 수
		int[] desktop = new int [101]; // 1-100 좌석
		int n = sc.nextInt(); // 손님의 수
		
		for(int i = 1; i < desktop.length; i++) {
			desktop[i] = 0; // 빈 좌석 --> 0
		}
		
		for(int j = 0; j < n; j++) {
			int wantDesk = sc.nextInt();
			
			if(desktop[wantDesk] == 0) { // 빈 좌석이면
				desktop[wantDesk] = 1; // 자리 있는 좌석 --> 1
			}else {
				count++; // 사람이 있는 자리면 count + 1;
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

}
