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
        Pattern pattern = Pattern.compile("(-?\\d+)");

        while ((str = br.readLine()) != null) {
            Matcher matcher = pattern.matcher(str);
            int[] parseInput = new int[4];
            for(int i = 0; matcher.find(); i++) {
                parseInput[i] = Integer.parseInt(matcher.group());
            }
            coordinates.add(new Coordinate(parseInput));
        }

        int xMax;   int xMin;
        int yMax;   int yMin;
        int xOldDiff = Integer.MAX_VALUE; int xNewDiff = Integer.MAX_VALUE;
        int yOldDiff = Integer.MAX_VALUE; int yNewDiff = Integer.MAX_VALUE;
        int time = 0;

        // Look for the moment that the xDiff and yDiff goes from decreasing to increasing
        do {
            xOldDiff = xNewDiff;
            yOldDiff = yNewDiff;
            xMax = Integer.MIN_VALUE; xMin = Integer.MAX_VALUE;
            yMax = Integer.MIN_VALUE; yMin = Integer.MAX_VALUE;

            for(Coordinate c : coordinates) {
                c.update(1);

                if(c.x > xMax) {
                    xMax = c.x;
                }
                if(c.x < xMin) {
                    xMin = c.x;
                }
                if(c.y > yMax) {
                    yMax = c.y;
                }
                if(c.y < yMin) {
                    yMin = c.y;
                }
            }
            time++;
            xNewDiff = xMax - xMin;
            yNewDiff = yMax - yMin;
        } while(xNewDiff < xOldDiff && yNewDiff < yOldDiff);

        xMax = Integer.MIN_VALUE; xMin = Integer.MAX_VALUE;
        yMax = Integer.MIN_VALUE; yMin = Integer.MAX_VALUE;

        // Go one step back, calculate new max/min
        for(Coordinate c : coordinates) {
            c.update(-1);
            if(c.x > xMax) {
                xMax = c.x;
            }
            if(c.x < xMin) {
                xMin = c.x;
            }
            if(c.y > yMax) {
                yMax = c.y;
            }
            if(c.y < yMin) {
                yMin = c.y;
            }
        }

    boolean hasFound = false;
        for(int y = yMin; y <= yMax; y++) {
            for(int x = xMin; x <= xMax; x++) {
                for(Coordinate c : coordinates) {
                    if(c.x == x && c.y == y) {
                        hasFound = true;
                        break;
                    }
                }
                if(hasFound) {
                    System.out.print("#");
                } else {
                    System.out.print(".");
                }
                hasFound = false;
            }
            System.out.println();
        }
        System.out.println(time - 1);
    }


}
