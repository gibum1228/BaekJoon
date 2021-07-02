import java.util.Scanner;

public class B11655 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str_result = sc.nextLine();

        for(int i = 0; i < str_result.length(); i++){
            if((str_result.charAt(i) >= 'a' && str_result.charAt(i) <= 'm') ||
                    (str_result.charAt(i) >= 'A' && str_result.charAt(i) <= 'M')){
                System.out.print((char)(str_result.charAt(i) + 13));
            }else if((str_result.charAt(i) >= 'n' && str_result.charAt(i) <= 'z') ||
                    (str_result.charAt(i) >= 'N' && str_result.charAt(i) <= 'Z')){
                System.out.print((char)(str_result.charAt(i) - 13));
            }else{
                System.out.print(str_result.charAt(i));
            }
        }
        
        sc.close();
    }
}
