import java.util.*;
import java.io.*;

public class d6 {
    public static void main(String[] args)throws Exception {
        // Read input
        File file = new File("inputTest.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<Coordinate> list = new ArrayList<Coordinate>();
        while ((str = br.readLine()) != null) {
            int x = Integer.parseInt(str.split(",")[0]);
            int y = Integer.parseInt(str.split(",")[1].substring(1));
            list.add(new Coordinate(x,y));
        }

        // Find the smallest x and y then
        int minX = Integer.MAX_VALUE;
        int minY = Integer.MAX_VALUE;
        for(Coordinate co : list) {
            System.out.println(co.toString());
            if(co.x < minX) {
                minX = co.x;
            }
            if(co.y < minY) {
                minY = co.y;
            }
        }
        //Shift all coordinates up to the right depending on the minX and minY found.
        for(Coordinate co : list) {
            co.x = co.x - minX;
            co.y = co.y - minY;
        }


    }
}
