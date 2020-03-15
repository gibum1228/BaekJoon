import java.util.Scanner;

public class B15963 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		Long n = sc.nextLong();
		Long m = sc.nextLong();
		
		if(n.compareTo(m) == 0) {
			System.out.println(1);
		}else {
			System.out.println(0);
		}

		sc.close();
	}

}
