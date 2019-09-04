/*
����
���� n���� �־����� ��, n���� ���� ���ϴ� �Լ��� �ۼ��Ͻÿ�.
�ۼ��ؾ� �ϴ� �Լ��� ������ ����.
C, C11, C (Clang), C11 (Clang): long long sum(int *a, int n);
a: ���� ���ؾ� �ϴ� ���� n���� ����Ǿ� �ִ� �迭 (0 �� a[i] �� 1,000,000, 1 �� n �� 3,000,000)
n: ���� ���ؾ� �ϴ� ������ ����
���ϰ�: a�� ���ԵǾ� �ִ� ���� n���� ��
C++, C++11, C++14, C++17, C++ (Clang), C++11 (Clang), C++14 (Clang), C++17 (Clang): long long sum(std::vector<int> &a);
a: ���� ���ؾ� �ϴ� ���� n���� ����Ǿ� �ִ� �迭 (0 �� a[i] �� 1,000,000, 1 �� n �� 3,000,000)
���ϰ�: a�� ���ԵǾ� �ִ� ���� n���� ��
Python 2, Python 3, PyPy, PyPy3: def solve(a: list) -> int
a: ���� ���ؾ� �ϴ� ���� n���� ����Ǿ� �ִ� ����Ʈ (0 �� a[i] �� 1,000,000, 1 �� n �� 3,000,000)
���ϰ�: a�� ���ԵǾ� �ִ� ���� n���� �� (����)
Java: long sum(int[] a); (Ŭ���� �̸�: Test)
a: ���� ���ؾ� �ϴ� ���� n���� ����Ǿ� �ִ� �迭 (0 �� a[i] �� 1,000,000, 1 �� n �� 3,000,000)
���ϰ�: a�� ���ԵǾ� �ִ� ���� n���� ��
Go: sum(a []int) int
a: ���� ���ؾ� �ϴ� ���� n���� ����Ǿ� �ִ� �迭 (0 �� a[i] �� 1,000,000, 1 �� n �� 3,000,000)
���ϰ�: a�� ���ԵǾ� �ִ� ���� n���� ��
 */
import java.util.Scanner;
import java.util.ArrayList;

public class B15596 {
	
	static long sum(int[] a) {
		int sum = 0;
		
		for(int i = 0; i < a.length; i++) {
			sum += a[i];
		}
		
		return sum;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc = new Scanner(System.in);
		
		ArrayList<Integer> digitList = new ArrayList<Integer>(1); 
		
		while(true) {
			try{
				int input = sc.nextInt();
				
				digitList.add(input);
			}
			catch (Exception e) {
				break;
			}
		}
		
		int[] a = new int [digitList.size()];
		for(int i = 0; i < a.length; i++) {
			a[i] = digitList.get(i);
		}
		System.out.println(sum(a));
		
		sc.close();
	}
	
}