import java.util.Scanner;

public class B10987 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int count = 0;
		String s = sc.next();
		
		for(int i = 0; i < s.length(); i++) {
			switch(s.charAt(i)) {
			case 'a':
			case 'e':
			case 'i':
			case 'o':
			case 'u':
				count++;
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

}
