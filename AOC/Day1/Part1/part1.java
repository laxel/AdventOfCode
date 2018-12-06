import java.io.*;

public class part1 {

    public static void main(String[] args)throws Exception {
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        int sum = 0;
        while ((st = br.readLine()) != null) {
            sum += Integer.parseInt(st);
        }
        System.out.println(sum);
    }
}
