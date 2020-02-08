import java.util.Scanner;

public class B5565 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int sum = sc.nextInt();
		
		for(int i = 0; i < 9; i++) {
			int n = sc.nextInt();
			sum -= n;
		}
		
		System.out.println(sum);
		
		sc.close();
	}

}
