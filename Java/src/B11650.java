import java.util.Scanner;
import java.util.Arrays;
import java.util.Comparator;

public class B11650 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[][] coordinate = new int [n][2];
		
		for(int i = 0; i < coordinate.length; i++) {
			coordinate[i][0] = sc.nextInt();
			coordinate[i][1] = sc.nextInt();
		}
		
		Arrays.sort(coordinate, new Comparator<int []>() {
			@Override
			public int compare(int[] o1, int[] o2) {
				if(o1[0] == o2[0]) {
					return Integer.compare(o1[1], o2[1]);
				}
				return Integer.compare(o1[0], o2[0]);
			}
		});
		
		for(int i = 0; i < n; i++) {
			System.out.println(coordinate[i][0] + " " + coordinate[i][1]);
		}
		
		sc.close();
	}

}
