/*
����
���ĺ� ��ҹ��ڷ� �� �ܾ �־�����, �� �ܾ�� ���� ���� ���� ���ĺ��� �������� �˾Ƴ��� ���α׷��� �ۼ��Ͻÿ�. ��, �빮�ڿ� �ҹ��ڸ� �������� �ʴ´�.
�Է�
ù° �ٿ� ���ĺ� ��ҹ��ڷ� �̷���� �ܾ �־�����. �־����� �ܾ��� ���̴� 1,000,000�� ���� �ʴ´�.
���
ù° �ٿ� �� �ܾ�� ���� ���� ���� ���ĺ��� �빮�ڷ� ����Ѵ�. ��, ���� ���� ���� ���ĺ��� ���� �� �����ϴ� ��쿡�� ?�� ����Ѵ�.
 */
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class B1157 {
	public static void main(String args[]) throws Exception {
		Scanner sc = new Scanner(System.in);
		String str = sc.next();
		int cnt = 1;//���ڼ�
		str = str.toUpperCase();//�빮�ڷ� �ٲ�
		char[] arr = str.toCharArray();
		ArrayList<Integer> com = new ArrayList<>();//�� ������ ���� �����迭
		ArrayList<Character> ans = new ArrayList<>();//�� ���ڸ� �����迭
		Arrays.sort(arr);//�빮�ڵ��� ����

		for (int i = 0; i < arr.length; i++) {
			if (i == arr.length - 1) {//����������
				ans.add(arr[i]);
				com.add(cnt);
			} else {
				if (arr[i] != arr[i + 1]) {
					ans.add(arr[i]);
					com.add(cnt);
					cnt = 1;
				} else {
					cnt++;
				}
			}
		}
		int max = 1;//������ ����
		int index = 0;//���� ������ ����ִ� com �迭�� �ε���
		cnt = 0;
		for (int i = 0; i < com.size(); i++) {
			max = Math.max(max, com.get(i));//���� ū ���ڸ� ã��
		}

		if (com.size() == 1) {//���� ���ڸ� �ִ� ���
			cnt = 1;
		} else {
			for (int i = 0; i < com.size(); i++) {
				if (com.get(i) == max) {//max���� ������� ī��Ʈ
					cnt++;
					index = i;
				}
			}
		}

		if (cnt != 1) {//���� ū ���ڰ� �Ѱ��� �ƴϸ� ����ǥ
			System.out.println("?");
		} else {
			System.out.println(ans.get(index));
		}
		
		sc.close();
	}
}