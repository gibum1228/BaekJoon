/*
����
�� ���� A, B, C�� �־�����. �̶�, �� ��°�� ū ������ ����ϴ� ���α׷��� �ۼ��Ͻÿ�. 
�Է�
ù° �ٿ� �� ���� A, B, C�� �������� ���еǾ� �־�����. (1 �� A, B, C �� 100)
���
�� ��°�� ū ������ ����Ѵ�.
 */
import java.util.Scanner;
import java.util.Arrays;

public class B10817 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int[] numList = new int [3];
		
		for(int i = 0; i < numList.length; i++) {
			numList[i] = sc.nextInt();
		}
		
		Arrays.sort(numList);
		
		System.out.println(numList[1]);
		
		sc.close();
	}

}
