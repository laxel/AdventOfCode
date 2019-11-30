import java.io.*;
import java.util.*;
import java.util.concurrent.TimeUnit;

public class d18 {

    public static final boolean print = false;

    public static void main(String[] args) throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        ArrayList<String> strList = new ArrayList<String>();

        while((str = br.readLine()) != null) {
            strList.add(str);
        }

        char[][] map = new char[strList.size()][strList.get(0).length()];
        for(int y = 0; y < strList.size(); y++) {
            for(int x = 0; x < strList.get(0).length(); x++) {
                map[x][y] = strList.get(y).charAt(x);
            }
        }

        ArrayList<Integer> patternList = new ArrayList<Integer>();

        for(int i = 0; i < 600; i++) {
            char[][] newMap = new char[map.length][map[0].length];
            // For every coordinate
            for(int y = 0; y < map.length; y++) {
                for(int x = 0; x < map[0].length; x++) {
                    int numTrees = 0;
                    int numLumber = 0;

                    // Check every adjecient coordinate
                    for(int yDiff = -1; yDiff < 2; yDiff++) {
                        for(int xDiff = -1; xDiff < 2; xDiff++) {
                            if(x+xDiff < map[0].length && x+xDiff >= 0
                              && y+yDiff < map.length && y+yDiff >= 0) {
                                char ch = map[x+xDiff][y+yDiff];
                                if(ch == '#') numLumber++;
                                if(ch == '|') numTrees++;
                            }
                        }
                    }
                    //System.out.println("x: " + x + ", y: " + y + " --> Trees: " +  numTrees + ", Lumber:  " + numLumber);


                    char ch = map[x][y];
                    if(ch == '.' && numTrees >= 3) {
                        newMap[x][y] = '|';
                    } else if(ch == '|') {
                        if(numLumber >= 3) {
                            newMap[x][y] = '#';
                        } else {
                            newMap[x][y] = '|';
                        }
                    } else if(ch == '#' && numTrees >= 1 && numLumber >= 2) {
                        newMap[x][y] = '#';
                    } else {
                        newMap[x][y] = '.';
                    }
                }
            }

            map = newMap;

            if(print) {
                TimeUnit.MILLISECONDS .sleep(100);
                System.out.print("\033[H\033[2J"); // clear screen

                for(int _y = 0; _y < map.length; _y++) {
                    for(int _x = 0; _x < map[0].length; _x++) {
                        System.out.print(map[_x][_y]);
                    }
                    System.out.println();
                }
                System.out.println(i);
            }

            // Used to find pattern in part2
            /*int numTrees = 0;
            int numLumber = 0;

            for(int y = 0; y < map.length; y++) {
                for(int x = 0; x < map[0].length; x++) {
                    if(map[x][y] == '|') {
                        numTrees++;
                    } else if(map[x][y] == '#') {
                        numLumber++;
                    }
                }
            }

            if(i >= 500 && i < 600) {
                patternList.add(numTrees*numLumber);
            }*/

        }

        for(int i = 0; i < patternList.size(); i++) {
            System.out.println((i+500) + ", " + patternList.get(i));
        }


        int numTrees = 0;
        int numLumber = 0;

        for(int y = 0; y < map.length; y++) {
            for(int x = 0; x < map[0].length; x++) {
                if(map[x][y] == '|') {
                    numTrees++;
                } else if(map[x][y] == '#') {
                    numLumber++;
                }
            }
        }

        System.out.println("/-------------- PART 1 --------------/");
        System.out.println(numTrees + " * " + numLumber + " = " + (numTrees*numLumber));
        System.out.println("/-------------- PART 1 --------------/");
        System.out.println("Calculate by hand >: (See pattern)");

    }
}
