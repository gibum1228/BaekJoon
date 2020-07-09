import java.util.Scanner;

public class B1259 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			String s = sc.next();
			if(s.compareTo("0") == 0) {
				break;
			}
			String reverseS = "";
			
			for(int i = s.length() - 1; i >= 0 ; i--) {
				reverseS += s.charAt(i);
			}
			
			if(s.compareTo(reverseS) == 0) {
				System.out.println("yes");
			}else {
				System.out.println("no");
			}
		}
		
		sc.close();
	}

}
