/*
����
���� ����Ʈ�ε��� �� ������ ���̰� 3, 4, 5�� �ﰢ���� ���� �ﰢ���ΰ��� �˾Ƴ´�. �־��� ������ ���̷� �ﰢ���� �������� �ƴ��� �����Ͻÿ�.
�Է�
�Է��� �������� �׽�Ʈ���̽��� �־����� �������ٿ��� 0 0 0�� �Էµȴ�. �� �׽�Ʈ���̽��� ��� 30,000���� ���� ���� ������ �־�����, �� �Է��� ���� ���̸� �ǹ��Ѵ�.
���
�� �Է¿� ���� ���� �ﰢ���� �´ٸ� "right", �ƴ϶�� "wrong"�� ����Ѵ�.
 */
import java.util.Scanner;

public class B4153 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int x, y, z; // ���� �ﰢ���� �� ��=
		
		while(true) {
			x = sc.nextInt(); // �� �� �Է¹ޱ�
			y = sc.nextInt();
			z = sc.nextInt();
			
			if( (x == 0 && y == 0) && z == 0) { // ���α׷� ����
				break;
			}
			
			int xy = (x * x) + (y * y);
			
			if(xy == (z * z)) { // ��Ÿ��� ���ǰ� �´��� Ȯ��
				System.out.println("right");
			}else {
				System.out.println("wrong");
			}
		}
		
		sc.close();
	}

}
