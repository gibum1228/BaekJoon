/*
����
������ ���� ��Ģ�� ������ �ڿ� ���� ��� ������.
�Է�
ù° �ٿ� N(1 �� N �� 100)�� �־�����.
���
ù° �ٺ��� 2��N-1��° �ٱ��� ���ʴ�� ���� ����Ѵ�.
 */
import java.io.*;

public class B2444 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int size = Integer.parseInt(br.readLine());
		
		for(int i = 1; i <= size; i++){ // ���� ���
			for(int j = 0; j < size - i; j++) {
				bw.write(" ");
			}
			for(int k = 1; k < i+i; k++) {
				bw.write("*");
			}
			bw.write("\n");
		}
		
		for(int i = size - 1; i > 0; i--) { // �Ʒ� ���
			for(int j = size; j > i; j--) {
				bw.write(" ");
			}
			for(int k = 1; k < i+i; k++) {
				bw.write("*");
			}
			bw.write("\n");
		}
		
		bw.flush(); // print
		bw.close();
		br.close();
	}

}
