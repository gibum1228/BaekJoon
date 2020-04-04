import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class B1764 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		HashSet setList = new HashSet();
		int n = sc.nextInt(); // 듣도 못한 사람
		int m = sc.nextInt(); // 보다 못한 사람
		ArrayList<String> sList = new ArrayList<String>();
		
		for(int i = 0; i < n; i++) { // 해쉬에 입력받기
			setList.add(sc.next());
		}
		
		for(int j = 0; j < m; j++) { // 셋 안에 같은 문자열이 있는지 확인
			String s = sc.next();
			
			if(setList.contains(s)) {
				sList.add(s);
			}
		}
 		
		Collections.sort(sList); // 순서대로 정렬
		
		System.out.println(sList.size());
		for(int k = 0; k < sList.size(); k++) {
			System.out.println(sList.get(k));
		}
		
		sc.close();
	}

}
