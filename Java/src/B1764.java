import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class B1764 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		HashSet setList = new HashSet();
		int n = sc.nextInt(); // �赵 ���� ���
		int m = sc.nextInt(); // ���� ���� ���
		ArrayList<String> sList = new ArrayList<String>();
		
		for(int i = 0; i < n; i++) { // �ؽ��� �Է¹ޱ�
			setList.add(sc.next());
		}
		
		for(int j = 0; j < m; j++) { // �� �ȿ� ���� ���ڿ��� �ִ��� Ȯ��
			String s = sc.next();
			
			if(setList.contains(s)) {
				sList.add(s);
			}
		}
 		
		Collections.sort(sList); // ������� ����
		
		System.out.println(sList.size());
		for(int k = 0; k < sList.size(); k++) {
			System.out.println(sList.get(k));
		}
		
		sc.close();
	}

}
