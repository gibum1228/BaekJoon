import java.util.Scanner;

public class B1550 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.next(); // 16진수 입력받기
		String[] cList = s.split(""); // 자릿수로 나누기
		int result = 0; // 10진수 값
		
		for(int i = cList.length - 1; i >= 0; i--) {
			switch(cList[i]) {
			case "A":
				result += (Math.pow(16, (cList.length - 1 - i)) * 10);
				break;
			case "B":
				result += (Math.pow(16, (cList.length - 1 - i)) * 11);
				break;
			case "C":
				result += (Math.pow(16, (cList.length - 1 - i)) * 12);
				break;
			case "D":
				result += (Math.pow(16, (cList.length - 1 - i)) * 13);
				break;
			case "E":
				result += (Math.pow(16, (cList.length - 1 - i)) * 14);
				break;
			case "F":
				result += (Math.pow(16, (cList.length - 1 - i)) * 15);
				break;
			default:
				result += (Math.pow(16, (cList.length - 1 - i)) * Integer.parseInt(cList[i]));
			}
		}
		
		System.out.println(result);
		
		sc.close();
	}

}
