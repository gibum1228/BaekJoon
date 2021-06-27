import java.io.BufferedReader;
import java.io.InputStreamReader;

public class B10816 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int N = Integer.parseInt(br.readLine());
        int[] arr = new int [20000001];

        String[] have = br.readLine().split(" ");
        for(String i : have){
            arr[10000000 + Integer.parseInt(i)] += 1;   
        }

        int M = Integer.parseInt(br.readLine());
        String[] count = br.readLine().split(" ");
        for(String i : count){
            sb.append(arr[10000000 + Integer.parseInt(i)] + " ");
        }

        System.out.println(sb.toString());

        br.close();
    }
}