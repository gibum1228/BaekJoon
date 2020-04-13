import java.util.Scanner;

public class B10808 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int[] alphabet = new int [26];
		String s = sc.next();
		char[] stoC = s.toCharArray();
		
		for(int k = 0; k < 26; k++) {
			alphabet[k] = 0;
		}
		
		for(int i = 0; i < stoC.length; i++) {
			int c = (int)stoC[i] - 97;
			alphabet[c] += 1;
		}
		
		for(int j = 0; j < alphabet.length; j++) {
			System.out.print(alphabet[j] + " ");
		}
		
		sc.close();
	}

}
