import java.util.Scanner;

public class B9093 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int tCase = sc.nextInt();
		sc.nextLine(); // 이거 안 쓰면 s[1]이 공백으로 씹힘  <- nextInt, nextLine 문제점 해결
		
		for(int i = 0; i < tCase; i++) {
			String s = sc.nextLine();
			String[] sList = s.split(" ");
			
			for(int j = 0; j < sList.length; j++) { // 공백으로 나눠진 갯수 만큼
				
				for(int k = sList[j].length() - 1; k >= 0; k--) { // 공백으로 split한 String 길이
					System.out.print(sList[j].charAt(k)); // 뒤에서부터 출력
				}
				System.out.print(" ");
			}
			System.out.println();
		}
		
		sc.close();
	}

}
