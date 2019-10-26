import java.util.Scanner;

public class B10886 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int zCount = 0; // 0 카운트
		int oCount = 0; // 1 카운트
		
		for(int i = 0; i < n; i++) {
			int count = sc.nextInt();
			if(count == 1) {
				oCount += 1;
			}else {
				zCount += 1;
			}
		}
		
		if(oCount > zCount) {
			System.out.println("Junhee is cute!");
		}else {
			System.out.println("Junhee is not cute!");
		}
		
		sc.close();
	}

}
