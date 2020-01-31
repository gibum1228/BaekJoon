import java.util.Scanner;

public class B2747 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int f1 = 0;
		int f2 = 1;
		int fn = 0;
		
		if(n == 1) {
			System.out.println(1);
		}else {
			for(int i = 0; i < n - 1; i++) { 
				fn = f1 + f2;
				f1 = f2;
				f2 = fn;
			}
			
			System.out.println(fn);
		}
		
		
		sc.close();
	}

}
