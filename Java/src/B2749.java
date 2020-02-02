/*
�Ǻ���ġ�� �Ӽ� :
1. �ǻ�� �ֱ� : �Ǻ���ġ ���� K�� ���� �������� �׻� �ֱ⸦ ������. (�Ǻ���ġ ���� 3���� �������� ��, �ֱ��� ���̴� 8 )
2. �ֱ��� ���̰� P�̸�, N��° �Ǻ���ġ ���� M���� ���� �������� N%P��° �Ǻ���ġ ���� M�� ���� �������� ����.
3. M = 10^k �� ��, k > 2 ���, �ֱ�� �׻� 15 x 10^k-1�̴�.
 */

import java.io.IOException;
import java.util.Scanner;

public class B2749 {

    public static void main(String[] args) throws IOException {

        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long[] arr;
        int mod = 1000000;
        int period = mod / 10 * 15;

        arr = new long[period];
        arr[0] = 0;
        arr[1] = 1;

        for(int i = 2; i < period; i++) {
            arr[i] = arr[i - 1] + arr[i - 2];
            arr[i] = arr[i] % mod;
        }

        int index = (int) (n % period);

        System.out.println(arr[index]);
        
        sc.close();
    }
}