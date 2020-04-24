import java.util.Scanner;

public class B1789 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		long s = sc.nextLong();
		long i = 1;
		long result = 0;
		int count = 0;
		
		while(true) {
			result += i;
			i++;
			
			if(result > s) {
				break;
			}else {
				count++;
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

}
