import java.util.Arrays;
import java.util.Scanner;

public class B2822 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int [8][2]; // 입력 저장
        int[] result = new int [5]; // 상위 5개 문제 저장
        int sum = 0;

        for(int i = 0; i < 8; i++){
            arr[i][0] = sc.nextInt();
            arr[i][1] = i + 1;
        }

        // 점수를 기준으로 저장
        Arrays.sort(arr, (int[] a, int[] b) -> {
            return b[0] - a[0];   
        });

        // 상위 5개의 합과 문제 저장
        for(int i = 0; i < 5; i++){
            sum += arr[i][0];
            result[i] = arr[i][1];
        }

        Arrays.sort(result);

        // 출력
        System.out.println(sum);
        for(int i = 0; i < 5; i++){
            System.out.print(result[i] + " ");
        }

        sc.close();
    }
}
