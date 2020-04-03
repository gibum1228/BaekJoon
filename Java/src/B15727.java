import java.util.Scanner;

public class B15727 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long l = sc.nextLong();
		
		if(l % 5 == 0) {
			System.out.println(l / 5);
		}else {
			System.out.println(l / 5 + 1);
		}
		
		sc.close();
	}

}
