/*
����
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
(�߷�)
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer. 
Go to the store and buy some more, 99 bottles of beer on the wall.
99 Bottles of Beer��� �뷡�� ����� Hello Worldó�� ���α׷��� ���� ������ ���� ���δ�. �츮�� ��ǥ�� N Bottles of Beer�� �θ��� ���̴�. 
����л��� ���ָ� ���ô� ���� ����� �̷��� ���� ��ġ�� �������� �ع����ſ� ���� ������ ������ ���ָ� ���ô� �� �ƴ϶� �뷡�� �θ��� �ǹǷ� ����� ����.
N Bottles of Beer�� ����� ���� ������ ���� ���������. ���� ���� K���� ���ְ� �ִٰ� ����. �� ó������ K = N�̴�. �̶� ���� �� ���� ���鼭 ������ ����Ѵ�.
K bottles of beer on the wall, K bottles of beer.
Take one down and pass it around, K-1 bottles of beer on the wall.
��, ���ְ� �� ���� ������ ǥ���Ϸ��� 1 bottles�� �ƴ϶� 1 bottle�̶�� �ؾ� �Ѵ�. ���� ���ְ� �� ���� ������ ǥ���Ϸ��� 0 bottles�� �ƴ϶� no more bottles��� �ؾ� �Ѵ�.
���ְ� ���� ���������� �� ������ �ݺ��ϰ�, �� �̻� �������� ������ ������ ����ϰ� �����Ѵ�. ���������� ���ָ� �� ���� ����� ��� 1 bottles�� �ƴ϶� 1 bottle�̶�� �ؾ� �Ѵ�.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, N bottles of beer on the wall.
�Է�
1 �̻� 99 ������ �ڿ��� N�� �־�����.
���
N Bottles of Beer�� ���縦 ����Ѵ�.
 */
import java.io.*;

public class B17293 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = n; i >= 0; i--) {
			if(i == 2) {
				bw.write("2 bottles of beer on the wall, 2 bottles of beer.\n");
				bw.write("Take one down and pass it around, 1 bottle of beer on the wall.\n\n");
				continue;
			}
			if(i == 1) {
				bw.write("1 bottle of beer on the wall, 1 bottle of beer.\n");
				bw.write("Take one down and pass it around, no more bottles of beer on the wall.\n\n");
				continue;
			}
			if(i == 0) {
				if(n == 1) { // ���ʿ� ���ֺ��� �� ���� �ܼ��� (n==1)
					bw.write("No more bottles of beer on the wall, no more bottles of beer.\n"); 
					bw.write("Go to the store and buy some more, " + n +" bottle of beer on the wall.");
				}else {
					bw.write("No more bottles of beer on the wall, no more bottles of beer.\n");
					bw.write("Go to the store and buy some more, " + n +" bottles of beer on the wall.");
				}
				continue;
			}
			
			bw.write(i + " bottles of beer on the wall, " + i + " bottles of beer.\n");
			bw.write("Take one down and pass it around, " + (i-1) + " bottles of beer on the wall.\n\n");
		}
		
		bw.flush();
		br.close();
		bw.close();
	}

}
