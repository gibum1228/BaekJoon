import java.io.*;
import java.util.ArrayList;
import java.util.Collections;

public class B2751 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		ArrayList<Integer> nList = new ArrayList<Integer>();
		
		for(int i = 0; i < n; i++) {
			nList.add(Integer.parseInt(br.readLine()));
		}
		
		Collections.sort(nList);
		
		for(int j = 0; j < nList.size(); j++) {
			System.out.println(nList.get(j));
		}
		
		br.close();
	}
	
}
