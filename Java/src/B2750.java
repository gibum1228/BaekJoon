/*
����
N���� ���� �־����� ��, �̸� ������������ �����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� ���� ���� N(1 �� N �� 1,000)�� �־�����. ��° �ٺ��� N���� �ٿ��� ���ڰ� �־�����. �� ���� ������ 1,000���� �۰ų� ���� �����̴�. ���� �ߺ����� �ʴ´�.
���
ù° �ٺ��� N���� �ٿ� ������������ ������ ����� �� �ٿ� �ϳ��� ����Ѵ�.
 */
import java.util.Scanner;
import java.util.Arrays;

public class B2750 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
	
		int size = sc.nextInt();
		int[] a = new int [size];
		
		for(int i = 0; i < size; i++) {
			a[i] = sc.nextInt();
		}
		
		Arrays.sort(a);
		
		for(int i = 0; i < size; i++) {
			System.out.println(a[i]);
		}
		
		sc.close();
	}

}
