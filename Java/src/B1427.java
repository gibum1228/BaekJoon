/*
����
�迭�� �����ϴ� ���� ����. ���� �־�����, �� ���� �� �ڸ����� ������������ �����غ���.
�Է�
ù° �ٿ� �����ϰ����ϴ� �� N�� �־�����. N�� 1,000,000,000���� �۰ų� ���� �ڿ����̴�.
���
ù° �ٿ� �ڸ����� ������������ ������ ���� ����Ѵ�.
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
