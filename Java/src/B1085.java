/*
����
�Ѽ��� ���� (x, y)�� �ִ�. ���簢���� ���� �Ʒ� �������� (0, 0)�� �ְ�, ������ �� �������� (w, h)�� �ִ�. 
���簢���� ��輱���� ���� �Ÿ��� �ּڰ��� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� x y w h�� �־�����. w�� h�� 1,000���� �۰ų� ���� �ڿ����̰�, x�� 1���� ũ�ų� ����, 
w-1���� �۰ų� ���� �ڿ����̰�, y�� 1���� ũ�ų� ����, h-1���� �۰ų� ���� �ڿ����̴�.
���
ù° �ٿ� ������ ������ ����Ѵ�.
 */
import java.util.Scanner;

public class B1085 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int x = sc.nextInt(); // �� �� �Է¹ޱ�
		int y = sc.nextInt();
		int w = sc.nextInt();
		int h = sc.nextInt();
		int xResult = 0; // �Ÿ� �ּҰ�
		int yResult = 0;
		
		if((w-x) > x) { // x�� ���� ª�� �Ÿ� ���ϱ�
			xResult = x;
		}else {
			xResult = w - x;
		}
		
		if((h-y) > y) { // y�� ���� ª�� �Ÿ� ���ϱ�
			yResult = y;
		}else {
			yResult = h - y;
		}
		
		if(xResult > yResult) { // �Ÿ� �ּҰ� ���ϱ�
			System.out.println(yResult);
		}else {
			System.out.println(xResult);
		}
		
		sc.close();
	}

}
