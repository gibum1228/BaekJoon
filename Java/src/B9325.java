/*
����
�غ��̴� �б��� �ٴϸ鼭 ƴƴ�� �� ������ �ڵ����� ����� �Ѵ�. �ڵ����� ���� ���� �ɼ��� ���Խ�ų �� �ִµ� �غ��̴� ������ ������ ���� ���ϱ� ������ ģ�� �¿��̿��� ������ û�ߴ�. 
������ �¿��̵� ������ ������ ���Ѵ�. �ҽ��� �� �� ģ���� ���� ��� �ɼ��� �־��� �ڵ����� �����ϴµ� �ʿ��� �׼��� ����� ����.
�Է�
ù° �ٿ� �׽�Ʈ ���̽��� ������ �־�����.
�� �׽�Ʈ ���̽��� ù �ٿ� �ڵ����� ���� s�� �־�����. (1 �� s �� 100 000)
��° �ٿ� �غ��̰� �����Ϸ��� �ϴ� ���� �ٸ� �ɼ��� ���� n�� �־�����. (0 �� n �� 1 000)
���̾� n���� ���� �Է����� ���´�. �� ���� q �� p�� �̷���� �ִµ� q�� �غ��̰� ����� �ϴ� Ư�� �ɼ��� �����̰� p�� �ش� �ɼ��� �����̴�. 
(1 �� q �� 100, 1 �� p �� 10 000)
���
�� �׽�Ʈ ���̽� ����, �غ��̰� ���������� �����Ϸ��� �ڵ����� ������ ���پ� ����Ѵ�.
 */
import java.util.Scanner;

public class B9325 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt(); // ���̽� ��
		
		for(int i = 0; i < size; i++) {
			int carPrice = sc.nextInt(); // �ڵ��� ���� ����
			int option = sc.nextInt();
			
			if(option == 0) {
				System.out.println(carPrice);
				continue;
			}
			
			for(int j = 0; j < option; j++) {
				int optionCount = sc.nextInt(); // �ɼ� ����
				int optionPrice = sc.nextInt(); // �ɼ� ����
				
				carPrice += (optionCount * optionPrice); // ����
			}
			
			System.out.println(carPrice);
		}
		
		sc.close();
	}

}
