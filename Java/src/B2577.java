/*
����
�� ���� �ڿ��� A, B, C�� �־��� �� A��B��C�� ����� ����� 0���� 9���� ������ ���ڰ� �� ���� ���������� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
���� ��� A = 150, B = 266, C = 427 �̶�� 
A �� B �� C = 150 �� 266 �� 427 = 17037300 �� �ǰ�, 
����� ��� 17037300 ���� 0�� 3��, 1�� 1��, 3�� 2��, 7�� 2�� ������.
�Է�
ù° �ٿ� A, ��° �ٿ� B, ��° �ٿ� C�� �־�����. A, B, C�� ��� 100���� ���ų� ũ��, 1,000���� ���� �ڿ����̴�.
���
ù° �ٿ��� A��B��C�� ����� 0 �� �� �� �������� ����Ѵ�. 
���������� ��° �ٺ��� �� ��° �ٱ��� A��B��C�� ����� 1���� 9������ ���ڰ� ���� �� �� �������� ���ʷ� �� �ٿ� �ϳ��� ����Ѵ�.
 */
import java.util.Arrays;
import java.util.Scanner;

public class B2577 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int[] countDigit = new int [10]; // 0���� 9���� ī��Ʈ �� �迭 ����
		Arrays.fill(countDigit, 0); // �迭 0���� ä���
		int a = sc.nextInt(); // �� ���� ����
		int b = sc.nextInt();
		int c = sc.nextInt();
		String mulDigit = "" + (a * b * c);
		
		for(int i = 0; i < mulDigit.length(); i++) {
			int j = mulDigit.charAt(i) - '0'; // char '1'���� char '0' ����
			countDigit[j] += 1;
		}
		
		for(int i = 0; i < countDigit.length; i++) {
			System.out.println(countDigit[i]);
		}
		
		sc.close();
	}

}
