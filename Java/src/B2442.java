/*
����
ù° �ٿ��� �� 1��, ��° �ٿ��� �� 3��, ..., N��° �ٿ��� �� 2��N-1���� ��� ����
���� ����� �������� ��Ī�̾�� �Ѵ�.
�Է�
ù° �ٿ� N(1 �� N �� 100)�� �־�����.
���
ù° �ٺ��� N��° �ٱ��� ���ʴ�� ���� ����Ѵ�.
 */
import java.io.*;

public class B2442 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int size = Integer.parseInt(br.readLine());
		
		for(int i = 1; i <= size; i++) {
			for(int j = size; j > i; j--) {
				bw.write(" ");
			}
			for(int k = 1; k < i+i; k++) {
				bw.write("*");
			}
			bw.write("\n");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}

}
