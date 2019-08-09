/*
문제
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
입력
첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
출력
첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class B1157 {
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		int cnt = 1;//글자수
		str = str.toUpperCase();//대문자로 바꿈
		char[] arr = str.toCharArray();
		ArrayList<Integer> com = new ArrayList<>();//각 글자의 수를 넣을배열
		ArrayList<Character> ans = new ArrayList<>();//각 글자를 넣을배열
		Arrays.sort(arr);//대문자들을 소팅

		for (int i = 0; i < arr.length; i++) {
			if (i == arr.length - 1) {//마지막글자
				ans.add(arr[i]);
				com.add(cnt);
			} else {
				if (arr[i] != arr[i + 1]) {
					ans.add(arr[i]);
					com.add(cnt);
					cnt = 1;
				} else {
					cnt++;
				}
			}
		}
		int max = 1;//글자의 개수
		int index = 0;//글자 개수가 들어있는 com 배열의 인덱스
		cnt = 0;
		for (int i = 0; i < com.size(); i++) {
			max = Math.max(max, com.get(i));//제일 큰 숫자를 찾음
		}

		if (com.size() == 1) {//같은 글자만 있는 경우
			cnt = 1;
		} else {
			for (int i = 0; i < com.size(); i++) {
				if (com.get(i) == max) {//max값이 몇개인지를 카운트
					cnt++;
					index = i;
				}
			}
		}

		if (cnt != 1) {//제일 큰 숫자가 한개가 아니면 물음표
			System.out.println("?");
		} else {
			System.out.println(ans.get(index));
		}
		
		sc.close();
	}
}