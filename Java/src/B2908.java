/*
����
������� ���� ����� ������ ���� ���Ѵ�. ����� ���ڸ� �дµ� ������ �ִ�. �̷��� ������ ���ϴ� ����� ���ؼ� ����̴� ���� ũ�⸦ ���ϴ� ������ ���־���. 
����̴� �� �ڸ� �� �� ���� ĥ�ǿ� ���־���. �� ������ ũ�Ⱑ ū ���� ���غ���� �ߴ�.
����� ���� �ٸ� ����� �ٸ��� �Ųٷ� �д´�. ���� ���, 734�� 893�� ĥ�ǿ� �����ٸ�, ����� �� ���� 437�� 398�� �д´�. 
����, ����� �� ���� ū ���� 437�� ū ����� ���� ���̴�.
�� ���� �־����� ��, ����� ����� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� ����̰� ĥ�ǿ� ���� �� �� A�� B�� �־�����. �� ���� ���� ���� �� �ڸ� ���̸�, 0�� ���ԵǾ� ���� �ʴ�.
���
ù° �ٿ� ����� ����� ����Ѵ�.
 */
import java.util.Scanner;

public class B2908 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		String a = sc.next(); // �Է¹��� �� �� a, b
		String b = sc.next();
		String changeString = ""; // �Ųٷ� �ٲ� ���� ������ ����
		char[] charList = {}; // �Ųٷ� �ٲٱ� ���� �迭
		
		charList = a.toCharArray();
		for(int i = charList.length - 1; i >= 0; i--) { // ���� �Ųٷ� �ٲٱ�
			changeString += charList[i];
		}
		a = changeString;
		
		charList = b.toCharArray();
		changeString = ""; // ���� �ʱ�ȭ
		for(int i = charList.length - 1; i >= 0; i--) {
			changeString += charList[i];
		}
		b = changeString;
		
		int intA = Integer.parseInt(a); // ���ڿ��� ���������� ��ȯ
		int intB = Integer.parseInt(b);
		
		if(intA > intB) { // a, b �� �� ū ���� ���
			System.out.println(intA);
		}else {
			System.out.println(intB);
		}
		
		sc.close();
	}

}
