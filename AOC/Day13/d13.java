import java.util.*;
import java.io.*;

public class d13 {
    public static void main(String[] args) throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<String> strList = new ArrayList<String>();
        int width = -1;

        while((str = br.readLine()) != null) {
            strList.add(str);
            if(str.length() > width) width = str.length();
        }

        char[][] map = new char[width][strList.size()];

        for(int y = 0; y < strList.size(); y++) {
            String strToParse = strList.get(y);
            for(int x = 0; x < strToParse.length(); x++) {
                char ch = strToParse.charAt(x);
                if(ch == 'v' || ch == '^') {
                    map[x][y] = '|';
                } else if(ch == '<' || ch == '>') {
                    map[x][y] = '-';
                } else {
                    map[x][y] = ch;
                }
            }
        }
    }
}
