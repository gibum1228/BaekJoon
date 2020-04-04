import java.util.Scanner;

public class B5554 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int h = 0, s = 0;
		
		for(int i = 0; i < 4; i++) {
			int n = sc.nextInt();
			
			if(n < 60) {
				s += n;
			}else {
				h += (n / 60);
				s += (n % 60);
			}
		}
		
		h += (s / 60);
		s %= 60;
		
		System.out.println(h);
		System.out.println(s);
		
		sc.close();
	}

}
