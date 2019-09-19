/*
문제
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.
1. 길이가 짧은 것부터
2. 길이가 같으면 사전 순으로
입력
첫째 줄에 단어의 개수 N이 주어진다. (1≤N≤20,000) 둘째 줄부터 N개의 줄에 걸쳐 알파벳 소문자로 이루어진 단어가 한 줄에 하나씩 주어진다. 
주어지는 문자열의 길이는 50을 넘지 않는다.
출력
조건에 따라 정렬하여 단어들을 출력한다. 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력한다.
 */
import java.util.Scanner;
import java.util.Arrays;

public class B1181 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt(); // 단어의 개수
		String[] wordNote = new String[size]; // 단어장
		
		for(int i = 0; i < size; i++) { // 단어 입력받기
			wordNote[i] = sc.next(); 
		}
		
		Arrays.sort(wordNote); // 단어 정렬
		// 단어 길이 별로 정렬하기
		String tmp; // 변경을 위한 변수
		for(int i = 0; i < size; i++) { // 단어를 조건에 맞게 정렬하기
			for(int j = 0; j < size; j++) {
				if(wordNote[i].length() > wordNote[j].length()) {
					tmp = wordNote[i];
					wordNote[i] = wordNote[j];
					wordNote[j] = tmp;
				} else if(wordNote[i].length() == wordNote[j].length()) {
					if(wordNote[i].compareTo(wordNote[j]) > 0) {
						tmp = wordNote[i];
						wordNote[i] = wordNote[j];
						wordNote[j] = tmp;
					}
				}
			}
		}
		
		for(int i = 0; i < size; i++) {
			System.out.println(wordNote[i]);
		}
		
		sc.close();
	}

}
