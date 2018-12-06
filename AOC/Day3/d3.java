import java.util.*;
import java.io.*;

public class d3 {
    public static void main(String[] args)throws Exception {
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String st;
        ArrayList<String> list = new ArrayList<String>();

        while ((st = br.readLine()) != null) {
            list.add(st);
        }

        int[] cordinates = new int[1000000];

        for(int i = 0; i < list.size(); i++) {
            String str = list.get(i);

            String strP1 = str.split("@ ")[1];
            String[] strP2 = strP1.split(",");
            Integer leftOff = Integer.parseInt(strP2[0]);
            String[] strP3 = strP2[1].split(": ");
            Integer uppOff = Integer.parseInt(strP3[0]);
            String[] strP4 = strP3[1].split("x");
            Integer width = Integer.parseInt(strP4[0]);
            Integer height = Integer.parseInt(strP4[1]);

            for(int w = 0; w < width; w++) {
                for(int h = 0; h < height; h++) {
                    cordinates[(uppOff+h) * 1000 + (leftOff + w)]++;
                }
            }
        }

        int numOverlap = 0;
        for(int n= 0; n < cordinates.length; n++) {
            if(cordinates[n] > 1) {
                numOverlap++;
            }
        }
        System.out.println("Amount of overlaps: " + numOverlap);


        // ----------------- PART 2 -----------------

        for(int i = 0; i < list.size(); i++) {
            String str = list.get(i);

            String strP1 = str.split("@ ")[1];
            String[] strP2 = strP1.split(",");
            Integer leftOff = Integer.parseInt(strP2[0]);
            String[] strP3 = strP2[1].split(": ");
            Integer uppOff = Integer.parseInt(strP3[0]);
            String[] strP4 = strP3[1].split("x");
            Integer width = Integer.parseInt(strP4[0]);
            Integer height = Integer.parseInt(strP4[1]);

            boolean isOverlapping = false;
            for(int w = 0; w < width; w++) {
                for(int h = 0; h < height; h++) {
                    if (cordinates[(uppOff+h) * 1000 + (leftOff + w)] != 1) {
                        isOverlapping = true;
                    }
                }
            }
            if(!isOverlapping) {
                System.out.println("ID that dosn't overlap: " + (i+1));
                return;
            }
        }

    }
}
