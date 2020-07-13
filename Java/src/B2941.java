import java.util.Scanner;

public class B2941 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		char[] cArray = sc.next().toCharArray(); // char �迭�� ����
		int count = 0; // ũ�ξ�Ƽ�� ����
		
		for(int i = 0; i < cArray.length; i++) {
			switch(cArray[i]) { // �� ���ǿ� �°� ����
			case 'c':
				if(i < cArray.length-1 && (cArray[i+1] == '=' || cArray[i+1] == '-')) {
					i++; // jumping
					count++;
					continue;
				}
				break;
				
			case 'd':
				if(i < cArray.length-1 && cArray[i+1] == '-') {
					i++;
					count++;
					continue;
				}else if(i < cArray.length-2 && cArray[i+1] == 'z' && cArray[i+2] == '=') {
					i+=2;
					count++;
					continue;
				}
				break;
				
			case 'l':
				if(i < cArray.length-1 && cArray[i+1] == 'j') {
					i++;
					count++;
					continue;
				}
				break;
				
			case 'n':
				if(i < cArray.length-1 && cArray[i+1] == 'j') {
					i++;
					count++;
					continue;
				}
				break;
				
			case 's':
				if(i < cArray.length-1 && cArray[i+1] == '=') {
					i++;
					count++;
					continue;
				}
				break;
				
			case 'z':
				if(i < cArray.length-1 && cArray[i+1] == '=') {
					i++;
					count++;
					continue;
				}
				break;
			}
			
			count++;
		}
		
		System.out.println(count);
		
		sc.close();
	}

}
