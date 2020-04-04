import java.util.Scanner;

public class B2914 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int a = sc.nextInt();
		int l = sc.nextInt();
		
		System.out.println(a * (l - 1) + 1);
		
		sc.close();
	}

}
