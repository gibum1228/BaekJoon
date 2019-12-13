import java.util.Scanner;

public class B1357 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		StringBuffer sb = new StringBuffer();
		
		String[] s = sc.nextLine().split(" ");
		sb.append(s[0]);
		String s1 = sb.reverse().toString();
		sb.delete(0, s[0].length());
		
		sb.append(s[1]);
		String s2 = sb.reverse().toString();
		sb.delete(0, s[1].length());
		
		int n = Integer.parseInt(s1) + Integer.parseInt(s2);
		
		String s3 = String.valueOf(n);
		sb.append(s3);
		sb.reverse();
		
		int result = Integer.parseInt(sb.toString());
		System.out.println(result);
		
		sc.close();
	}

}
