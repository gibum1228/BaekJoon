/*
����
���ĺ� �ҹ��ڷ� �̷���� N���� �ܾ ������ �Ʒ��� ���� ���ǿ� ���� �����ϴ� ���α׷��� �ۼ��Ͻÿ�.
1. ���̰� ª�� �ͺ���
2. ���̰� ������ ���� ������
�Է�
ù° �ٿ� �ܾ��� ���� N�� �־�����. (1��N��20,000) ��° �ٺ��� N���� �ٿ� ���� ���ĺ� �ҹ��ڷ� �̷���� �ܾ �� �ٿ� �ϳ��� �־�����. 
�־����� ���ڿ��� ���̴� 50�� ���� �ʴ´�.
���
���ǿ� ���� �����Ͽ� �ܾ���� ����Ѵ�. ��, ���� �ܾ ���� �� �Էµ� ��쿡�� �� ������ ����Ѵ�.
 */
import java.util.Scanner;
import java.util.Arrays;

public class B1181 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt(); // �ܾ��� ����
		String[] wordNote = new String[size]; // �ܾ���
		
		for(int i = 0; i < size; i++) { // �ܾ� �Է¹ޱ�
			wordNote[i] = sc.next(); 
		}
		
		Arrays.sort(wordNote); // �ܾ� ����
		// �ܾ� ���� ���� �����ϱ�
		String tmp; // ������ ���� ����
		for(int i = 0; i < size; i++) { // �ܾ ���ǿ� �°� �����ϱ�
			for(int j = 0; j < size; j++) {
				if(wordNote[i].length() > wordNote[j].length()) {
					tmp = wordNote[i];
					wordNote[i] = wordNote[j];
					wordNote[j] = tmp;
				} else if(wordNote[i].length() == wordNote[j].length()) {
					if(wordNote[i].compareTo(wordNote[j]) > 0) {
						tmp = wordNote[i];
						wordNote[i] = wordNote[j];
						wordNote[j] = tmp;
					}
				}
			}
		}
		
		for(int i = 0; i < size; i++) {
			System.out.println(wordNote[i]);
		}
		
		sc.close();
	}

}
