import java.io.*;

public class part1 {

    public static void main(String[] args)throws Exception {
        File file = new File("/Users/axelkarlsson/Documents/AOC/Day1/Part1/input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        int sum = 0;
        while ((st = br.readLine()) != null) {
            sum += Integer.parseInt(st);
        }
        System.out.println(sum);
    }
}
