import java.util.*;
import java.io.*;

public class d9 {
    public static void main(String[] args) throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<Integer> list = new ArrayList<Integer>();

        while ((str = br.readLine()) != null) {
            String[] strList = str.split(" ");
            for(String s : strList) {
                list.add(Integer.parseInt(s));
            }
        }
    }
}
