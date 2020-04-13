import java.util.Scanner;

public class B2525 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int hour = sc.nextInt(); // 시
		int min = sc.nextInt(); // 분
		int time = sc.nextInt(); // 걸리는 시간
		
		min = min + time;
		
		if(min >= 60) {
			hour = hour + (min / 60);
			min = min % 60;
		}
		
		if(hour > 23) {
			hour = hour - ((hour / 24 )* 24);
		}
		
		System.out.println(hour + " " + min);
		
		sc.close();
	}

}
