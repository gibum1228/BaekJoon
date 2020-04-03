import java.util.Scanner;

public class B2845 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		long l = sc.nextLong();
		long p = sc.nextLong();
		long[] nList = new long [5];
		
		for(int i = 0; i < 5; i++) {
			nList[i] = sc.nextLong();
		}
		
		System.out.println((nList[0] - (l * p)) + " " + (nList[1] - (l * p)) + " " + (nList[2] - (l * p)) + " " + (nList[3] - (l * p)) + " " + (nList[4] - (l * p)));
		
		sc.close();
	}

}
