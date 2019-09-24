/*
����
������ ���� ��Ģ�� ������ �ڿ� ���� ��� ������.
�Է�
ù° �ٿ� N�� �־�����. N�� �׻� 3�� �������� ���̴�. (3, 9, 27, ...) (N=3k, 1 �� k < 8)
���
ù° �ٺ��� N��° �ٱ��� ���� ����Ѵ�.
 */
import java.util.Arrays;
import java.util.Scanner;

public class B2447 {

	static char[][] board;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		long start = System.currentTimeMillis();
		Scanner sc = new Scanner(System.in);
		
		int size = sc.nextInt(); // 3�� ������
		board = new char [size][size];
		
		for(int i = 0; i < size; i++) {
			Arrays.fill(board[i], ' '); // �迭 �������� ä���
		}
		
		DrawStar(0, 0, size); // ����Լ� ����
		
		for(int i = 0; i < size; i++) {
			System.out.println(board[i]); // 2���� �迭 ���
		}
		
		sc.close();
	}

	public static void DrawStar(int x, int y, int size) { // ����Լ�
		if(size == 1) { // * ����ϱ�
			board[x][y] = '*';
			return;
		}
		
		int divN = size / 3; // 3�� ������
		for(int i = 0; i < 3; i++) {
			for(int j = 0; j < 3; j++) {
				if(i == 1 && j == 1) { // ���� �����
					continue;
				}
				
				DrawStar(x + (i * divN), y + (j * divN), divN);
			}
		}
	}
}
