import java.io.*;
import java.util.ArrayList;

public class B1181 { // �� �ܾ� ������ �������� �����ϴ� �迭�� ����� �� ���� �� ���� ex) jump table

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // ���� ������� ���� ���� ���
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int n = Integer.parseInt(br.readLine()); // �۵� Ƚ��
		ArrayList<String> word = new ArrayList<String>(); // ���ĵ� �ܾ ���� ArrayList
		
		for(int i = 0; i < n; i++) {
			String text = br.readLine(); // �ܾ� �Է� �ޱ�
			
			if(word.isEmpty()) { // �迭�� ��� ������ add
				word.add(text);
			}else { // �迭�� ��� ���� ������ �����ϱ� ���� sortWord() ȣ��
				sortWord(word, text);
			}
		}
		
		for(int i = 0; i < word.size(); i++) { // ���
			bw.write(word.get(i) + "\n");
		}
		
		bw.flush();
		bw.close();
		br.close();
	}

	static public void sortWord(ArrayList<String> word, String text) {
		for(int i = 0; i < word.size(); i++) {
			if(word.get(i).compareTo(text) == 0) { // �ߺ� �ܾ� ��ŵ
				break;
			}
			
			if(word.get(i).length() > text.length()) { // text�� ���̰� �� ª�� ���
				
				String tmp = word.get(i); // ��ȯ
				word.set(i, text);
				word.add(i+1, tmp);
				
				break;
			}else if(word.get(i).length() == text.length()){ // ���̰� ���� ���
				
				if(word.get(i).compareTo(text) < 0) { // text�� �ܾ� ������ �ڿ� ���� ���
					if(i != word.size() - 1) { // ������ �ܾ�� ���ϴ°� �ƴϸ�
						if(word.get(i+1).length() == text.length()) { // ���� �ܾ�� text�� ���̰� ���ٸ� ���� �ܾ�� ��
							continue;
						}
					}
					
					word.add(i+1, text); // �ٷ� ������ �߰�
				}else { // text �ܾ� ���� �� ���� ���
					String tmp = word.get(i); // ��ȯ
					word.set(i, text);
					word.add(i+1, tmp);
				}
				
				break;
			}else {
				
				if(i == word.size() - 1) { // ��ο� ������ �� text�� ���̰� ���� �� �� �� �ڿ� ����
					word.add(i+1, text);
				}
			}
		}
	}
}
