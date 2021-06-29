import java.util.Scanner;

public class B1018 {

    static boolean[][] arr;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int min = 64; // 다시 칠해야 되는 정사각형의 최소 개수, 초기화는 최대 칠할 개수로 함
        int N = sc.nextInt();
        int M = sc.nextInt();
        arr = new boolean [N][M];

        // input
        for(int i = 0; i < N; i++){
            String strLine = sc.next();

            for(int j = 0; j < M; j++){
                // White라면 True, Black이라면 False
                if(strLine.charAt(j) == 'W'){
                    arr[i][j] = true;
                }else{
                    arr[i][j] = false;
                }
            }
        }
        
        // 연산
        for(int i = 0; i <= N - 8; i++){
            for(int j = 0; j <= M - 8; j++){
                min = change(i, j, min);
            }
        }

        // result print
        System.out.println(min);

        sc.close();
    }

    public static int change(int row, int col, int min){
        int count = 0;
        boolean tf = arr[row][col]; // 첫 시작 바닥 색

        for(int i = row; i < row + 8; i++){
            for(int j = col; j < col + 8; j++){
                if(arr[i][j] != tf){ // 다르면 색상 바꿔야 하니 카운트++
                    count++;
                }

                tf = !tf; // 색상 바꿔줌
            }

            tf = !tf; // 라인 바꼈으니 색상 바꿔줌
        }

        /*
        첫 번째 칸을 기준으로 할 때 다시 색칠 할 수(count)와
        첫 번째 칸에 반대되는 색을 기준으로 할 때(64 - count)를 비교
        */
        count = Math.min(count, 64 - count);

        return Math.min(min, count);
    }
}
