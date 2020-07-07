import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;


public class B10989 {

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		int[] sortList = new int [10001];
		
		for(int i = 0; i < n; i++) {
			sortList[Integer.parseInt(br.readLine())]++;
		}
		
		for(int i = 1; i <= 10000; i++) {
			if(sortList[i] > 0) {
				for(int j = 0; j < sortList[i]; j++) {
					bw.write(Integer.toString(i) + "\n");
//					bw.flush();
				}
			}
		}
		
//		bw.flush();
		br.close();
		bw.close();
	}

}
