import java.util.Scanner;

public class B1977 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int m = sc.nextInt(); // m에서
		int n = sc.nextInt(); // n까지의 완전제곱수 구하기
		int min = 0; // 완전제곱수 최소값
		int sum = 0; // 완전제곱수 총합
		
		for(int i = 1; i * i <= n; i++) { // 완전제곱수가 n보다 작거나 같으면
			if(i*i >= m && i*i <= n) { // 완전 제곱수가 m-n 사이면
				if(min == 0) { // 최소 완전제곱수 구하기
					min = i*i;
				}
				sum += i*i; // 완전제곱수 총합 구하기
			}
		}
		
		if(min == 0) { // 완전제곱수가 하나도 없으면
			System.out.println("-1");
		}else { 
			System.out.println(sum);
			System.out.println(min);
		}
		
		sc.close();
	}

}
