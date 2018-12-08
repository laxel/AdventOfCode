import java.util.*;
import java.io.*;

public class d6 {
    public static void main(String[] args)throws Exception {
        // Read input
        File file = new File("inputTest.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<String> list = new ArrayList<String>();
        while ((str = br.readLine()) != null) {
            list.add(str);
        }
    }
}
