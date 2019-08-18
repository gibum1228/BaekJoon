/*
++++++++++++ �����佺�׳׽��� ü
����
M�̻� N������ �Ҽ��� ��� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� �ڿ��� M�� N�� �� ĭ�� ���̿� �ΰ� �־�����. (1 �� M �� N �� 1,000,000)
���
�� �ٿ� �ϳ���, �����ϴ� ������� �Ҽ��� ����Ѵ�.
 */
import java.util.Scanner;

public class B1929 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int minN = sc.nextInt(); // �ּ�
		int maxN = sc.nextInt(); // �ִ�
		int[] digitList = new int [maxN+1]; // maxN������ �迭
		
		for(int i = 2; i < digitList.length; i++) { // 2���� �迭 ���̱��� ���� �ֱ�
			digitList[i] = i;
		}
		
		for(int i = 2; i< digitList.length; i++) {  // ����� 0�ֱ�
			if(digitList[i] == 0) {  // i�� ����� �̹� 0�̸� ��ŵ
				continue;
			}
			for(int j = i+i; j < digitList.length; j += i) { // ����� �ε����� 0 �ֱ�
					digitList[j] = 0;
			}
		}
		
		for(int i = minN; i < digitList.length; i++) { // �Ҽ��� �ε��� ���
			if(digitList[i] != 0) {
				System.out.println(digitList[i]);
			}
		}
		
		sc.close();
	}

}
