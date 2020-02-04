/*
피보나치의 속성 :
1. 피사노 주기 : 피보나치 수를 K로 나눈 나머지는 항상 주기를 가진다. (피보나치 수를 3으로 나누었을 때, 주기의 길이는 8 )
2. 주기의 길이가 P이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같다.
3. M = 10^k 일 때, k > 2 라면, 주기는 항상 15 x 10^k-1이다.
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