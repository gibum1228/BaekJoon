import java.util.HashSet;
import java.util.Scanner;

public class B1920 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		boolean same;
		HashSet nList = new HashSet();
		
		// 입력받기
		int n = sc.nextInt();
		for(int i = 0; i < n; i++) {
			int num = sc.nextInt();
			nList.add(num);
		}
		int m = sc.nextInt();
		int[] mList = new int [m];
		for(int j = 0; j < m; j++) {
			int num = sc.nextInt();
			mList[j] = num;
		}
		
		// 비교하기
		for(int k = 0; k < m; k++) {
			same = false;
			if(nList.contains(mList[k])) {
				same = true;
			}
			if(same) {
				System.out.println(1);
			}else {
				System.out.println(0);
			}
		}
		
		sc.close();
	}

}
