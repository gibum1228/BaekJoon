import java.util.Scanner;

public class B10173 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			String s = sc.nextLine();
			if(s.compareTo("EOI") == 0){
				break;
			}
			
			s = s.toUpperCase();
			
			String[] checkNemo = s.split(" ");
			
			for(int i = 0; i < checkNemo.length; i++) {
				if(checkNemo[i].compareTo("NEMO") == 0 || checkNemo[i].compareTo("NEMO,") == 0 || checkNemo[i].compareTo("NEMO.") == 0) {
					System.out.println("Found");
					break;
				}
				
				if(i == (checkNemo.length - 1)) {
					System.out.println("Missing");
				}
			}
		}
				
		sc.close();
	}

}
