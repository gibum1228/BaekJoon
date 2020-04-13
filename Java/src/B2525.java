import java.util.Scanner;

public class B2525 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int hour = sc.nextInt(); // ��
		int min = sc.nextInt(); // ��
		int time = sc.nextInt(); // �ɸ��� �ð�
		
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
