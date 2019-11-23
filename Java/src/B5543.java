import java.util.Scanner;

public class B5543 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		int firBug = sc.nextInt();
		int secBug = sc.nextInt();
		int thrBug = sc.nextInt();
		int coca = sc.nextInt();
		int saida = sc.nextInt();
		int cheapBug = 0;
		int cheapJuice;
		
		if(firBug <= secBug && firBug <= thrBug) {
			cheapBug = firBug;
		}
		if(secBug <= firBug && secBug <= thrBug) {
			cheapBug = secBug;
		}
		if(thrBug <= firBug && thrBug <= secBug) {
			cheapBug = thrBug;
		}
		
		if(coca <= saida) {
			cheapJuice = coca;
		}else {
			cheapJuice = saida;
		}
		
		System.out.println(cheapBug + cheapJuice - 50);
		
		sc.close();
	}

}
