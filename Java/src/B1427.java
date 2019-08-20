/*
문제
배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.
입력
첫째 줄에 정렬하고자하는 수 N이 주어진다. N은 1,000,000,000보다 작거나 같은 자연수이다.
출력
첫째 줄에 자리수를 내림차순으로 정렬한 수를 출력한다.
 */
import java.util.Scanner;
import java.util.Arrays;

public class B1427 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine();
		
		int size = s.length();
		char[] charList = new char [size];
		
		for(int i = 0; i < size; i++) {
			charList[i] = s.charAt(i);
		}
		
		Arrays.sort(charList);
		
		for(int i = size-1; i >= 0; i--) {
			System.out.print(charList[i]);
		}
		
		sc.close();
	}

}
