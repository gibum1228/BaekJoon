import java.util.Scanner;

public class B2864 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		String[] s = sc.nextLine().split(" ");
		String s1 = s[0], s2 = s[1];
		int min = 0, max = 0;
		
		min = Integer.parseInt(s[0].replace('6', '5')) + Integer.parseInt(s[1].replace('6', '5'));
		max = Integer.parseInt(s1.replace('5', '6')) + Integer.parseInt(s2.replace('5', '6'));
		
		System.out.println(min + " " + max);
		
		sc.close();
	}

}
