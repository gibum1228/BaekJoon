/*
����
������׷��� �����͸� �ð������� ǥ���� ���̴�. ����� �����Ǹ� �� ������ ���̴� ������ ���� ũ�⸦ ��Ÿ����. �Ϻ� �����Ͱ� �־����� ������׷��� �����Ͻÿ�.
�Է�
ù ��° �ٿ��� �׽�Ʈ ���̽��� ���� n (1 �� n �� 100)�� �־�����. ���� n ���� �ٿ��� �� ������׷��� ũ�� k (1 �� k �� 80)�� �־�����.
���
�� �׽�Ʈ ���̽��� ���ؼ� ������׷��� ũ�� k�� ������ ���� '='�� ����Ѵ�. '='���̿� ������ �������� �ʴ´�.
 */
import java.io.*;

public class B13752 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int size = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < size; i++) {
			int a = Integer.parseInt(br.readLine());
			
			for(int j = 0; j < a; j++) {
				bw.write("=");
			}
			
			bw.write("\n");
		}
		
		bw.flush();
		br.close();
		bw.close();
	}

}
