/*
����
�ڿ��� A, B�� �־����� A+B�� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
�ڿ��� A, B (0 < A, B �� 10)�� ù ��° �ٿ� �־�����. ��, �� ���� ���̿��� ������ �־����� �ʴ´�. �� ���� �տ� ���ʿ��� 0�� �ٴ� ���� ����.
���
ù ��° �ٿ� A+B�� ���� ����Ѵ�.
 */
import java.io.*;

public class B15873 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] s = br.readLine().split(""); // 1 < a, b <= 10

		int s1num = Integer.parseInt(s[1]); // �߰��� 0�� ���� ���������� �ٲ� ����, �ڿ��� �������� ��
		
		if(s.length == 4) {
			int a = Integer.parseInt(s[0]+s[1]);
			int b = Integer.parseInt(s[2]+s[3]);
			bw.write(a+b+"");
		}else if(s.length == 3) {
			if(s1num != 0) { // �߰��� 0�� ���� Ȯ���� �� �ְ� ����
				int a = Integer.parseInt(s[0]);
				int b = Integer.parseInt(s[1]+s[2]);
				bw.write(a+b+"");
			}else {
				int a = Integer.parseInt(s[0]+s[1]);
				int b = Integer.parseInt(s[2]);
				bw.write(a+b+"");
			}
		}else {
			int a = Integer.parseInt(s[0]);
			int b = Integer.parseInt(s[1]);
			bw.write(a+b+"");
		}
		
		bw.flush();
		
		br.close();
		bw.close();
	}

}
