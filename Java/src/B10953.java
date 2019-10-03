/*
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. A와 B는 콤마(,)로 구분되어 있다. (0 < A, B < 10)
출력
각 테스트 케이스마다 A+B를 출력한다.
 */
import java.io.*;

public class B10953 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int size = Integer.parseInt(br.readLine());
		
		for(int i = 0; i < size; i++) {
			String[] s = br.readLine().split(",");
			
			int a = Integer.parseInt(s[0]);
			int b = Integer.parseInt(s[1]);
			
			bw.write(a + b + "\n");
		}
		
		bw.flush();
		
		br.close();
		bw.close();
	}

}
