import java.util.*;
import java.io.*;

public class part1 {

    public static void main(String[] args)throws Exception {
        File file = new File("/Users/axelkarlsson/Documents/AOC/Day2/Part1/input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        int numTwo = 0;
        int numThree = 0;

        while ((st = br.readLine()) != null) {
            HashMap<Character, Integer> letters = new HashMap<Character, Integer>();

            for(Character c : st.toCharArray()) {
                if(letters.containsKey(c)) {
                    int n = letters.get(c);
                    letters.put(c,n+1);
                } else {
                    letters.put(c,1);
                }
            }

            Collection values = letters.values();
            if(values.contains(2)) {
                numTwo++;
            }
            if(values.contains(3)) {
                numThree++;
            }
        }
        System.out.println(numTwo + " * " + numThree + " = " + (numTwo * numThree));
    }
}
