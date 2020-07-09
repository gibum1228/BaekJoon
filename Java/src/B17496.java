import java.util.Scanner;

public class B17496 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt(); // 여름 일 수
		int t = sc.nextInt(); // 씨앗 자라는 일 수
		int c = sc.nextInt(); // 씨앗 심을 수 있는 칸 수
		int price = sc.nextInt(); // 한 개 당 가격
		
		int result = ((n - 1) / t) * c * price; // 총 수익
		
		System.out.println(result);
		
		sc.close();
	}

}
