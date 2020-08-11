import java.io.*;
import java.util.ArrayList;

public class B1181 { // 각 단어 길이의 시작점을 저장하는 배열을 만들면 더 좋을 거 같음 ex) jump table

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 빠른 입출력을 위해 버퍼 사용
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine()); // 작동 횟수
		ArrayList<String> word = new ArrayList<String>(); // 정렬된 단어를 담을 ArrayList
		
		for(int i = 0; i < n; i++) {
			String text = br.readLine(); // 단어 입력 받기
			
			if(word.isEmpty()) { // 배열이 비어 있으면 add
				word.add(text);
			}else { // 배열이 비어 있지 않으면 정렬하기 위해 sortWord() 호출
				sortWord(word, text);
			}
		}
		
		for(int i = 0; i < word.size(); i++) { // 출력
			bw.write(word.get(i) + "\n");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}

	static public void sortWord(ArrayList<String> word, String text) {
		for(int i = 0; i < word.size(); i++) {
			if(word.get(i).compareTo(text) == 0) { // 중복 단어 스킵
				break;
			}
			
			if(word.get(i).length() > text.length()) { // text의 길이가 더 짧을 경우
				
				String tmp = word.get(i); // 교환
				word.set(i, text);
				word.add(i+1, tmp);
				
				break;
			}else if(word.get(i).length() == text.length()){ // 길이가 같을 경우
				
				if(word.get(i).compareTo(text) < 0) { // text가 단어 순으로 뒤에 있을 경우
					if(i != word.size() - 1) { // 마지막 단어와 비교하는게 아니면
						if(word.get(i+1).length() == text.length()) { // 다음 단어와 text와 길이가 같다면 다음 단어와 비교
							continue;
						}
					}
					
					word.add(i+1, text); // 바로 다음에 추가
				}else { // text 단어 순이 더 앞일 경우
					String tmp = word.get(i); // 교환
					word.set(i, text);
					word.add(i+1, tmp);
				}
				
				break;
			}else {
				
				if(i == word.size() - 1) { // 모두와 비교했을 때 text의 길이가 가장 길 때 맨 뒤에 삽입
					word.add(i+1, text);
				}
			}
		}
	}
}
