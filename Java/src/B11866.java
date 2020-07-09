import java.util.Scanner;
import java.util.ArrayList;

public class B11866 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt(); // 1~n�� ���� 
		int k = sc.nextInt(); // jump ��
		int[] oneToN = new int [n+1]; // 1~n�� �����ϴ� �迭
		ArrayList<Integer> sequence = new ArrayList<Integer>(); // �似Ǫ�� ����

		for(int i = 0; i < n+1; i++) { // 1~n ����
			oneToN[i] = i;
		}
		
		int index = 1; // index ������ 1
		for(int a = 1; a <= n; a++) { // n��ŭ
			
			int b = 0; // k�� �Ǵ��� ����
			while(true) {
				if(b == k) { // k��ŭ �������� while ���� 
					break;
				}
				
				if(oneToN[index] == -1) { // �̹� �鸰 ���ڸ�
					index++; // ���� ���� ���� ���� ĭ���� �Ѿ��
					if(index > n) {
						index %= n;
					}
					continue;
				}
				
				if(b == k-1) { // 0~k-1�� k����ŭ ������ ����.
					sequence.add(oneToN[index]); // ������ ���� �ְ�
					
					oneToN[index] = -1; // index �� -1�� ������ �̹� �鸰 �ε������ �� ǥ��
				}
				
				index++; // ���� �ε����� ����
				if(index > n) { // index ���� ����
					index %= n;
				}

				b++;
			}
		}
		
		System.out.print("<"); // print
		for(int i = 0; i < sequence.size(); i++) {
			if(i == sequence.size()-1) {
				System.out.println(sequence.get(i) + ">");
			}else {
				System.out.print(sequence.get(i) + ", ");
			}
		}
		
		sc.close();
	}

}
