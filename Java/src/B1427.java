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
import java.util.List;
import java.util.Collections;

public class B1427 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		String text = sc.nextLine();
		String[] charList = text.split("");
		
		for(int i = 0; i < charList.length; i++) {
			System.out.println(charList[i]);
		}
		
		List<String> List = Arrays.asList(charList);
		
		Collections.reverse(List);
		
		for(int i = 0; i < List.size(); i++) {
			System.out.print(List.get(i));
		}
		
		sc.close();
	}

}
