/*
����)
���ĺ� �ҹ��ڷθ� �̷���� �ܾ� S�� �־�����. ������ ���ĺ��� ���ؼ�, �ܾ ���ԵǾ� �ִ� ��쿡�� ó�� �����ϴ� ��ġ��, ���ԵǾ� ���� ���� ��쿡�� -1�� ����ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�)
ù° �ٿ� �ܾ� S�� �־�����. �ܾ��� ���̴� 100�� ���� ������, ���ĺ� �ҹ��ڷθ� �̷���� �ִ�.
���)
������ ���ĺ��� ���ؼ�, a�� ó�� �����ϴ� ��ġ, b�� ó�� �����ϴ� ��ġ, ... z�� ó�� �����ϴ� ��ġ�� �������� �����ؼ� ����Ѵ�.
����, � ���ĺ��� �ܾ ���ԵǾ� ���� �ʴٸ� -1�� ����Ѵ�. �ܾ��� ù ��° ���ڴ� 0��° ��ġ�̰�, �� ��° ���ڴ� 1��° ��ġ�̴�.
 */
import java.util.Scanner;

public class B10809 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int copyChar = -1;
		int[] result = new int [26];
		String s = sc.nextLine();
		
		s = s.toLowerCase();
		for(int i = 0; i < result.length; i++) {
			result[i] = -1;
		}
		
		for(int i = 0; i < s.length(); i++) {
			int startChar = (int)s.charAt(i) - 97;
			if(startChar == copyChar) {
				continue;
			}else {
				result[startChar] = i;
			}
			copyChar = startChar;
		}
		/*
		a�� �ƽ�Ű �ڵ� 97
		z�� �ƽ�Ű �ڵ� 122
		 */
		for(int i = 0; i < result.length; i++) {
			System.out.print(result[i] + " ");
		}
		
		sc.close();
	}

}
