/*
����
�� N���� �־����� ��, N���� ���� ���ϴ� ���α׷��� �ۼ��Ͻÿ�.
�Է�
ù° �ٿ� �׽�Ʈ ���̽��� ���� T�� �־�����. �� �׽�Ʈ ���̽��� �� �ٷ� �̷���� ������, N(1 �� N �� 100)���� ���� �������� ���еǾ �־�����. 
�Է����� �־����� ���� 10,000���� �۰ų� ���� �ڿ����̴�. ��, 0���� �����ϴ� ���� �־����� �ʴ´�.
���
�� �׽�Ʈ ���̽����� �Է¹��� �� N���� ���� �� �ٿ� �ϳ��� �Է¹��� ������� ����Ѵ�.
 */
import java.util.StringTokenizer;
import java.io.*;

public class B11024 {

	public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        int tc = Integer.parseInt(bf.readLine());
        
        while(tc-- != 0) {
            int sum = 0;
            st = new StringTokenizer(bf.readLine());
            
            while(st.hasMoreTokens()) {
                sum += Integer.parseInt(st.nextToken());
            }
            
            System.out.println(sum);
        }
    }
}
