import java.util.Scanner;

public class B1977 {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int m = sc.nextInt(); // m����
		int n = sc.nextInt(); // n������ ���������� ���ϱ�
		int min = 0; // ���������� �ּҰ�
		int sum = 0; // ���������� ����
		
		for(int i = 1; i * i <= n; i++) { // ������������ n���� �۰ų� ������
			if(i*i >= m && i*i <= n) { // ���� �������� m-n ���̸�
				if(min == 0) { // �ּ� ���������� ���ϱ�
					min = i*i;
				}
				sum += i*i; // ���������� ���� ���ϱ�
			}
		}
		
		if(min == 0) { // ������������ �ϳ��� ������
			System.out.println("-1");
		}else { 
			System.out.println(sum);
			System.out.println(min);
		}
		
		sc.close();
	}

}
