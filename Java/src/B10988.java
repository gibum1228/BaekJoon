import java.util.Scanner;

public class B10988 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine();
		String rS = new StringBuffer(s).reverse().toString();
		
		if(s.compareTo(rS) == 0) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}
		
		sc.close();
	}

	
}
