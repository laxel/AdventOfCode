import java.io.*;
import java.util.*;

public class part2 {

    public static void main(String[] args)throws Exception {
        File file = new File("/Users/axelkarlsson/Documents/AOC/Day1/Part1/input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        ArrayList<Integer> input = new ArrayList<Integer>();
        while ((st = br.readLine()) != null) {
            input.add(Integer.parseInt(st));
        }

        int sum = 0;
        int i = 0;
        HashSet<Integer> fq = new HashSet<Integer>();

        while (true) {

            if(i >= input.size())
                i = 0;

            sum += input.get(i);
            if(!fq.add(sum)) {
                System.out.println(sum);
                break;
            }

            i++;
        }
    }
}
