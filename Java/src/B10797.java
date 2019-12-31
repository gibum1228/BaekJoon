import java.util.Scanner;

public class B10797 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int day = sc.nextInt();
		int carDate;
		int count = 0;
		
		for(int i = 0; i < 5; i++) {
			carDate = sc.nextInt();
			
			if(day == carDate) {
				count++;
			}
		}
		
		System.out.println(count);
		
		sc.close();
	}

}
