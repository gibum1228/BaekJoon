/*
����
9���� ���� �ٸ� �ڿ����� �־��� ��, �̵� �� �ִ��� ã�� �� �ִ��� �� ��° �������� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
���� ���, ���� �ٸ� 9���� �ڿ���
3, 29, 38, 12, 57, 74, 40, 85, 61
�� �־�����, �̵� �� �ִ��� 85�̰�, �� ���� 8��° ���̴�.
�Է�
ù ° �ٺ��� ��ȩ ��° �ٱ��� �� �ٿ� �ϳ��� �ڿ����� �־�����. �־����� �ڿ����� 100 ���� �۴�.
���
ù° �ٿ� �ִ��� ����ϰ�, ��° �ٿ� �ִ��� �� ��° �������� ����Ѵ�.
 */
import java.util.Scanner;

public class B2562 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int[] nArray = new int [9]; // 9���� ������ ���� �迭 ����
		
		for(int i = 0; i < nArray.length; i++) { // ���� �Է� �ޱ�
			nArray[i] = sc.nextInt();
		}
		
		int max = nArray[0]; // �ִ񰪰� �� ������ ������ �ʱ�ȭ
		int index = 1;
		
		for(int i = 1; i < nArray.length; i++) { // �ִ� ã�Ƴ��� �ִ��� �� ��° �������� ����
			if(max < nArray[i]) {
				max = nArray[i];
				index = i + 1;
			}
		}
		
		System.out.println(max); // ���
		System.out.println(index);
		
		sc.close();
	}

}
