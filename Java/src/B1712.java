/*
����
�������ڴ� ��Ʈ���� �����ϰ� �Ǹ��ϴ� ȸ���̴�. ��Ʈ�� �Ǹ� ����� ������� �ų� �Ӵ��, ��꼼, �����, �޿� �� A������ ���� ����� ���,
 �� ���� ��Ʈ���� �����ϴ� ������ ����� �ΰǺ� �� �� B������ ���� ����� ��ٰ� �Ѵ�.
���� ��� A=1,000, B=70�̶�� ����. �� ��� ��Ʈ���� �� �� �����ϴ� ���� �� 1,070������ ���, �� �� �����ϴ� ���� �� 1,700������ ���.
��Ʈ�� ������ C�������� å���Ǿ��ٰ� �Ѵ�. �Ϲ������� ���� ����� �÷� ���� ���� ��� ���� �� ����(�Ǹź��)�� �� ���(=�������+�������)���� �������� �ȴ�.
���ʷ� �� ������ �� ��뺸�� ������ ������ �߻��ϴ� ������ ���ͺб���(BREAK-EVEN POINT)�̶�� �Ѵ�.
A, B, C�� �־����� ��, ���ͺб����� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� A, B, C�� �� ĭ�� ���̿� �ΰ� ������� �־�����. A, B, C�� 21�� ������ �ڿ����̴�.
���
ù ��° �ٿ� ���ͺб��� �� ���ʷ� ������ �߻��ϴ� �Ǹŷ��� ����Ѵ�. ���ͺб����� �������� ������ -1�� ����Ѵ�.
 */
import java.io.*;
import java.util.*;

public class B1712 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        StringTokenizer st = new StringTokenizer(br.readLine());
        long A = Integer.parseInt(st.nextToken());
        long B = Integer.parseInt(st.nextToken());
        long C = Integer.parseInt(st.nextToken());
        
        if((C - B) > 0) {
            bw.write(((A / (C - B)) + 1) + "\n");
        } else {
            bw.write("-1\n");
        }

        bw.flush();
        br.close();
        bw.close();
	}

}
