/*
문제
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.
입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
출력
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.
 */
import java.io.*;

public class B2444 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int size = Integer.parseInt(br.readLine());
		
		for(int i = 1; i <= size; i++){ // 위에 출력
			for(int j = 0; j < size - i; j++) {
				bw.write(" ");
			}
			for(int k = 1; k < i+i; k++) {
				bw.write("*");
			}
			bw.write("\n");
		}
		
		for(int i = size - 1; i > 0; i--) { // 아래 출력
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
