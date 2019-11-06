/*
문제
자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.
입력
자연수 A, B (0 < A, B ≤ 10)가 첫 번째 줄에 주어진다. 단, 두 수의 사이에는 공백이 주어지지 않는다. 두 수의 앞에 불필요한 0이 붙는 경우는 없다.
출력
첫 번째 줄에 A+B의 값을 출력한다.
 */
import java.io.*;

public class B15873 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		String[] s = br.readLine().split(""); // 1 < a, b <= 10

		int s1num = Integer.parseInt(s[1]); // 중간에 0만 따로 정수형으로 바꾼 다음, 뒤에서 조건으로 비교
		
		if(s.length == 4) {
			int a = Integer.parseInt(s[0]+s[1]);
			int b = Integer.parseInt(s[2]+s[3]);
			bw.write(a+b+"");
		}else if(s.length == 3) {
			if(s1num != 0) { // 중간에 0을 따로 확인할 수 있게 만듦
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
