/*
����
�ڿ��� M�� N�� �־��� �� M�̻� N������ �ڿ��� �� �Ҽ��� ���� ��� ��� �̵� �Ҽ��� �հ� �ּڰ��� ã�� ���α׷��� �ۼ��Ͻÿ�.
���� ��� M=60, N=100�� ��� 60�̻� 100������ �ڿ��� �� �Ҽ��� 61, 67, 71, 73, 79, 83, 89, 97 �� 8���� �����Ƿ�, �̵� �Ҽ��� ���� 620�̰�, �ּڰ��� 61�� �ȴ�.
�Է�
�Է��� ù° �ٿ� M��, ��° �ٿ� N�� �־�����.
M�� N�� 10,000������ �ڿ����̸�, M�� N���� �۰ų� ����.
���
M�̻� N������ �ڿ��� �� �Ҽ��� ���� ��� ã�� ù° �ٿ� �� ����, ��° �ٿ� �� �� �ּڰ��� ����Ѵ�. 
��, M�̻� N������ �ڿ��� �� �Ҽ��� ���� ���� ù° �ٿ� -1�� ����Ѵ�.
 */
import java.util.Scanner;
import java.util.ArrayList;

public class B2581 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Integer> primeList = new ArrayList<Integer>();
		int minN = sc.nextInt();
		int maxN = sc.nextInt();
		int count = 0;
		int addPrime = 0;
		
		for(int i = minN; i <= maxN; i++) {
			for(int j = 1; j <= i; j++) {
				if(i % j == 0) {
					count++;
				}
			}
			if(count == 2){
				primeList.add(i);
			}
			count = 0;
		}
		
		for(int i = 0; i < primeList.size(); i++) {
			addPrime += primeList.get(i);
		}
		
		System.out.println(addPrime);
		System.out.println(primeList.get(0));
		
		sc.close();
	}

}
