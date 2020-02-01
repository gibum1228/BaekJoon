import java.io.*;

public class B2748 {

	public static void main(String[] args) throws IOException{
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		long[] fac = new long [91];
		fac[0] = 0;
		fac[1] = 1;
		
		for(int i = 2; i <= n; i++) {
			fac[i] = fac[i-1] + fac[i-2];
		}
		
		bw.write(String.valueOf(fac[n]));
		
		bw.flush();

	}

}
