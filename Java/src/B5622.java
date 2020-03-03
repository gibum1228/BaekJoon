import java.util.Scanner;

public class B5622 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String[] s = sc.nextLine().split("");
		int size = s.length;
		
		for(int i = 0; i < s.length; i++) {
			switch(s[i]) {
			case "A":
			case "B":
			case "C":
				size += 2;
				break;
			case "D":
			case "E":
			case "F":
				size += 3;
				break;
			case "G":
			case "H":
			case "I":
				size += 4;
				break;
			case "J":
			case "K":
			case "L":
				size += 5;
				break;
			case "M":
			case "N":
			case "O":
				size += 6;
				break;
			case "P":
			case "Q":
			case "R":
			case "S":
				size += 7;
				break;
			case "T":
			case "U":
			case "V":
				size += 8;
				break;
			case "W":
			case "X":
			case "Y":
			case "Z":
				size += 9;
			}
		}
		
		System.out.println(size);
		
		sc.close();
	}

}
