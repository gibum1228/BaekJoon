/*
문제
99 bottles of beer on the wall, 99 bottles of beer.
Take one down and pass it around, 98 bottles of beer on the wall.
98 bottles of beer on the wall, 98 bottles of beer.
Take one down and pass it around, 97 bottles of beer on the wall.
(중략)
1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.
No more bottles of beer on the wall, no more bottles of beer. 
Go to the store and buy some more, 99 bottles of beer on the wall.
99 Bottles of Beer라는 노래의 가사는 Hello World처럼 프로그래밍 연습 예제로 자주 쓰인다. 우리의 목표는 N Bottles of Beer를 부르는 것이다. 
고등학생이 맥주를 마시는 것은 세계로 미래로 꿈을 펼치는 선린인의 준법정신에 맞지 않지만 정말로 맥주를 마시는 게 아니라 노래만 부르면 되므로 상관은 없다.
N Bottles of Beer의 가사는 다음 과정을 통해 만들어진다. 현재 벽에 K병의 맥주가 있다고 하자. 맨 처음에는 K = N이다. 이때 맥주 한 병을 따면서 다음을 출력한다.
K bottles of beer on the wall, K bottles of beer.
Take one down and pass it around, K-1 bottles of beer on the wall.
단, 맥주가 한 병만 있음을 표현하려면 1 bottles가 아니라 1 bottle이라고 해야 한다. 또한 맥주가 한 병도 없음을 표현하려면 0 bottles가 아니라 no more bottles라고 해야 한다.
맥주가 아직 남아있으면 위 과정을 반복하고, 더 이상 남아있지 않으면 다음을 출력하고 종료한다. 마찬가지로 맥주를 한 병만 사오는 경우 1 bottles가 아니라 1 bottle이라고 해야 한다.
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, N bottles of beer on the wall.
입력
1 이상 99 이하의 자연수 N이 주어진다.
출력
N Bottles of Beer의 가사를 출력한다.
 */
import java.io.*;

public class B17293 {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine());
		
		for(int i = n; i >= 0; i--) {
			if(i == 2) {
				bw.write("2 bottles of beer on the wall, 2 bottles of beer.\n");
				bw.write("Take one down and pass it around, 1 bottle of beer on the wall.\n\n");
				continue;
			}
			if(i == 1) {
				bw.write("1 bottle of beer on the wall, 1 bottle of beer.\n");
				bw.write("Take one down and pass it around, no more bottles of beer on the wall.\n\n");
				continue;
			}
			if(i == 0) {
				if(n == 1) { // 애초에 맥주병이 한 개면 단수임 (n==1)
					bw.write("No more bottles of beer on the wall, no more bottles of beer.\n"); 
					bw.write("Go to the store and buy some more, " + n +" bottle of beer on the wall.");
				}else {
					bw.write("No more bottles of beer on the wall, no more bottles of beer.\n");
					bw.write("Go to the store and buy some more, " + n +" bottles of beer on the wall.");
				}
				continue;
			}
			
			bw.write(i + " bottles of beer on the wall, " + i + " bottles of beer.\n");
			bw.write("Take one down and pass it around, " + (i-1) + " bottles of beer on the wall.\n\n");
		}
		
		bw.flush();
		br.close();
		bw.close();
	}

}
