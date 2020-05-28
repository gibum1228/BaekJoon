import java.util.Scanner;

public class B1316 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 테스트 케이스
		int count = 0; // 그룹 단어 갯수
		
		for(int i = 0; i < n; i++) {
			String s = sc.next();
			if(checkWord(s)) { // 그룹 단어 체커
				count++;
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

	public static boolean checkWord(String s) {
		
		boolean[] alphabet = new boolean [26]; // 연속되지 않는 중복된 단어가 있는지 판단하기 위한 배열
		
		for(int i = 0; i < s.length(); i++) {
			char text = s.charAt(i); // i번째 단어 체크
			
			if(alphabet[text - 'a']) { // 이미 체크된 알파벳이면 false 리턴
				return false;
			}else {
				if(i < s.length()-1 && text != s.charAt(i+1)) { // i번째 해당하는 알파벳의 연속이 끝나는 시점에 true 넣기
					alphabet[text - 'a'] = true;
				}
			}
		}
		
		return true; // 마지막까지 중복된 단어가 없을 경우 true 리턴
	}
}
