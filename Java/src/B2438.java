import java.util.*;

public class B2438 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
    
        int b2438 = sc.nextInt();
		    for(int i = 0; i < b2438; i++) {
			    for(int j = 0; j <= i; j++) {
				    System.out.print("*");
			    }
			    System.out.print("\n");
		    }
    }
}