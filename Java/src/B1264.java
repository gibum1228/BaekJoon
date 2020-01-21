import java.util.Scanner;

public class B1264 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		while(true) {
			String s = sc.nextLine();
			int wordCount = 0;
			if(s.compareTo("#") == 0) {
				sc.close();
				break;
			}
			
			s = s.toLowerCase();
			
			for(int i = 0; i < s.length(); i++) {
				switch (s.charAt(i)){
				case 'a':
					wordCount++;
					break;
				case 'e':
					wordCount++;
					break;
				case 'i':
					wordCount++;
					break;
				case 'o':
					wordCount++;
					break;
				case 'u':
					wordCount++;
				}
			}
			
			System.out.println(wordCount);
		}
		
	}

}
