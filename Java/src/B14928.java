import java.io.*;

public class B14928 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String input = br.readLine();
		int now = 0; // 자리수
		final int mod = 20000303; // 20000303으로 나눔
		
		for(int i = 0; i < input.length(); i++) {
			int n = input.charAt(i) - '0'; // char -> int 변환
			now *= 10; // 자리수 증가
			now += n;
			now %= mod;
		}
		
		System.out.println(now);
		
		br.close();
	}
}
