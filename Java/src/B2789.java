import java.util.Scanner;

public class B2789 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine();
		
		for(int i = 0; i < s.length(); i++) {
			switch(s.charAt(i)) {
			case 'C':
			case 'A':
			case 'M':
			case 'B':
			case 'R':
			case 'I':
			case 'D':
			case 'G':
			case 'E':
				continue;
			default:
				System.out.print(s.charAt(i));
			}
		}
		
		sc.close();
	}

}
