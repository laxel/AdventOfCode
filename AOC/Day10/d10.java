import java.util.*;
import java.io.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class d10 {
    public static void main(String[] args) throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        ArrayList<Coordinate> coordinates = new ArrayList<Coordinate>();
        String str;
        Pattern pattern = Pattern.compile("\\d{1,10}");


        while ((str = br.readLine()) != null) {
            /*int x = str.split("<")[1].split(",")[0];
            int x = str.split(",")[1].split(",")[0];*/
            Matcher matcher = pattern.matcher(str);
            if (matcher.find()) {
                System.out.println(matcher.group(0));
            }
        }
    }
}
