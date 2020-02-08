import java.util.Scanner;

public class B5585 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int price = sc.nextInt();
		int changeM = 1000 - price;
		int changeC = 0;
		
		while(changeM > 0) {
			if(changeM >= 500) {
				changeM -= 500;
				changeC++;
			}else if(changeM >= 100) {
				changeM -= 100;
				changeC++;
			}else if(changeM >= 50) {
				changeM -= 50;
				changeC++;
			}else if(changeM >= 10) {
				changeM -= 10;
				changeC++;
			}else if(changeM >= 5) {
				changeM -= 5;
				changeC++;
			}else {
				changeM -= 1;
				changeC++;
			}
		}
		
		System.out.println(changeC);
		
		sc.close();
	}

}
