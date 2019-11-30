import java.io.*;
import java.util.*;
import java.awt.Point;

public class d20 {
    public static void main(String[] args) throws Exception {
        // --- Read input ---
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        ArrayList<Character> input = new ArrayList<Character>();
        String str = br.readLine();

        for(int i = 1; i < str.length()-1; i++) {
            input.add(str.charAt(i));
        }


        Stack<Point> st = new Stack<Point>();
        Stack<Integer> st_dist = new Stack<Integer>();
        HashMap<Point, Integer> map = new HashMap<Point, Integer>();

        Point p = new Point(0,0);

        int distance = 0;
        int maxDist = 0;
        int atleast1000 = 0;

        for(char c : input) {

            switch(c) {
                case 'N':
                    p.y--;
                    distance++;
                    break;
                case 'E':
                    p.x++;
                    distance++;
                    break;
                case 'S':
                    p.y++;
                    distance++;
                    break;
                case 'W':
                    p.x--;
                    distance++;
                    break;
                case '(':
                    st.push((Point)p.clone());
                    st_dist.push(distance);
                    break;
                case '|':
                    p = st.peek();
                    distance = st_dist.peek();
                    break;
                case ')':
                    if(!st.empty()) {
                        p = st.pop();
                        distance = st_dist.pop();
                    }
                    break;
            }

            if(!map.containsKey(p)) {
                map.put(new Point(p.x, p.y), distance);
                if(distance > maxDist) {
                    maxDist = distance;
                }
                if(distance > 1000) {
                    atleast1000++;
                }
            }
        }
        System.out.println(maxDist);
        System.out.println(atleast1000);


    }
}
