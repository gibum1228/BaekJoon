import java.util.Scanner;

public class B5086 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			int firstInt = sc.nextInt();
			int secondInt = sc.nextInt();
			if(firstInt == 0 && secondInt == 0) {
				break;
			}
			
			if(secondInt % firstInt == 0) {
				System.out.println("factor");
			}else if(firstInt % secondInt == 0){
				System.out.println("multiple");
			}else {
				System.out.println("neither");
			}
		}
		
		sc.close();
	}

}
