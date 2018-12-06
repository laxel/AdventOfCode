import java.util.*;
import java.io.*;

public class d2p2 {

    public static void main(String[] args)throws Exception {
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        ArrayList<String> list = new ArrayList<String>();

        while ((st = br.readLine()) != null) {
            list.add(st);
        }

        for(int i = 0; i < list.size(); i++) {
            String word1 = list.get(i);

            for(int j = i + 1; j < list.size(); j++) {
                String word2 = list.get(j);
                int numWrong = 0;

                for(int n = 0; n < word1.length(); n++) {
                    if(word1.charAt(n) != word2.charAt(n)) {
                        numWrong++;
                    }

                    if(numWrong >= 2) {
                        break;
                    }
                }
                if(numWrong < 2) {
                    for(int p = 0; p < word1.length(); p++) {
                        if(word1.charAt(p) == word2.charAt(p)) {
                            System.out.print(word1.charAt(p));
                        }
                    }
                    System.out.println();
                    return;
                }

            }

        }

    }
}
