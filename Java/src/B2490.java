/*
����)
�츮���� ������ �����̴� �� ���� ��¦�� ������ ��(0)�� ��(1)�� ������ ���ڸ� ���� ��, ��, ��, ��, �� �����Ѵ�. 
�� �� ��¦�� ������ ���� �� ��¦�� �� Ȥ�� �� ������ �־��� �� ��(�� �� ��, �� �� ��), ��(�� �� ��, �� �� ��), ��(�� �� ��, �� �� ��), ��(�� �� ��), ��(�� �� ��) �� � �������� �����ϴ� ���α׷��� �ۼ��϶�.
�Է�)
ù° �ٺ��� ��° �ٱ��� �� �ٿ� ���� �� �� ���� ��¦���� ���¸� ��Ÿ���� �� ���� ����(0 �Ǵ� 1)��  ��ĭ�� ���̿� �ΰ� �־�����.
���)
ù° �ٺ��� ��° �ٱ��� �� �ٿ� �ϳ��� �����  ���� A, ���� B, ���� C, ���� D, ��� E�� ����Ѵ�.
 */
import java.util.Scanner;

public class B2490 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		int[] save = new int [4];
		int score;
		
		for(int i = 0; i < 3; i++) {
			score = 0;
			for(int j = 0; j < save.length; j++) {
				save[j] = sc.nextInt();
			}
			for(int j = 0; j < save.length; j++) {
				if(save[j] == 0) {
					score++;
				}
			}
			switch(score) {
			case 1:
				System.out.println("A");
				break;
			case 2:
				System.out.println("B");
				break;
			case 3:
				System.out.println("C");
				break;
			case 4:
				System.out.println("D");
				break;
			case 0:
				System.out.println("E");
			}
		}
		
		sc.close();
		
	}

}
