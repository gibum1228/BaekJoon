import java.io.*;

public class B15894 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		bw.write(Integer.parseInt(br.readLine()) * 4L + ""); // ¸Ç ¹Øº¯ * 4 == µÑ·¹
		
		bw.flush();
		br.close();
		bw.close();
	}

}
