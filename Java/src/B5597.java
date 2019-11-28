import java.util.Scanner;
import java.util.Vector;

public class B5597 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		Vector<Integer> checkL = new Vector<Integer>();
		
		for(int i = 1; i <= 30; i++) {
			checkL.add(i);
		}
		
		for(int i = 0; i < 28; i++) {
			int n = sc.nextInt();
			checkL.removeElement(n);
		}
		
		for(int i = 0; i < checkL.size(); i++) {
			System.out.println(checkL.get(i));
		}
		
		sc.close();
	}

}
