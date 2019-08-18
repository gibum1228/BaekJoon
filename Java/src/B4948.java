/*
����
����Ʈ�� ������ ������ �ڿ��� n�� ���Ͽ�, n���� ũ��, 2n���� �۰ų� ���� �Ҽ��� ��� �ϳ� �����Ѵٴ� ������ ��� �ִ�.
�� ������ ������ ����Ʈ���� 1845�⿡ �����߰�, ������Ƽ ü������� 1850�⿡ �����ߴ�.
���� ���, 10���� ũ��, 20���� �۰ų� ���� �Ҽ��� 4���� �ִ�. 
(11, 13, 17, 19) ��, 14���� ũ��, 28���� �۰ų� ���� �Ҽ��� 3���� �ִ�. (17,19, 23)
n�� �־����� ��, n���� ũ��, 2n���� �۰ų� ���� �Ҽ��� ������ ���ϴ� ���α׷��� �ۼ��Ͻÿ�. 
�Է�
�Է��� ���� ���� �׽�Ʈ ���̽��� �̷���� �ִ�. �� ���̽��� n�� �����ϸ�, �� �ٷ� �̷���� �ִ�. (n �� 123456)
�Է��� ���������� 0�� �־�����.
���
�� �׽�Ʈ ���̽��� ���ؼ�, n���� ũ��, 2n���� �۰ų� ���� �Ҽ��� ������ ����Ѵ�.
 */
import java.util.*;

public class B4948 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		
		while(true) {
			int minN = sc.nextInt(); // �ּ�
			if(minN == 0) {
				break;
			}
			int maxN = 2 * minN; // �ִ�
			int[] digitList = new int [maxN+1]; // maxN������ �迭
			int count = 0; // �Ҽ� ���� �� ����
			
			for(int i = 2; i < digitList.length; i++) { // 2���� �迭 ���̱��� ���� �ֱ�
				digitList[i] = i;
			}
			
			for(int i = 2; i < digitList.length; i++) {  // ����� 0�ֱ�
				if(digitList[i] == 0) {  // i�� ����� �̹� 0�̸� ��ŵ
					continue;
				}
				for(int j = i+i; j < digitList.length; j += i) { // ����� �ε����� 0 �ֱ�
						digitList[j] = 0;
				}
			}
			
			for(int i = minN + 1; i < digitList.length; i++) { // �Ҽ� ���� ���� < minN���� ũ�� maxN���� �۰ų� ���� >
				if(digitList[i] != 0) {
					count++;
				}
			}
			
			System.out.println(count);
		}
		
		sc.close();
	}

}
