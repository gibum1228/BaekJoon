import java.util.ArrayList;
import java.util.Scanner;

public class B1158 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();
        ArrayList<Integer> arr = new ArrayList<>();
        String result = "";

        // arr init
        for(int i = 1; i <= N; i++){
            arr.add(i);
        }

        int j = -1;
        for(int i = 0; i < N; i++){
            j = (j + K) % arr.size(); // K만큼 jumping
            
            result += arr.get(j); // 제거한 순서대로 출력

            if(i != N-1){ // format print
                result += ", ";
            }

            arr.remove(j); // 값 제거
            j -= 1; // 길이도 줄었으니 인덱스도 -1
        }

        System.out.println("<" + result + ">");

        sc.close();
    }
}
