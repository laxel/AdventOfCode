import java.util.*;
import java.io.*;
import java.util.concurrent.TimeUnit;

public class d15 {
    public static final String ANSI_RED = "\u001B[31m";
    public static final String ANSI_GREEN = "\u001B[32m";
    public static final String ANSI_WHITE = "\u001B[37m";

    public static final boolean print = false;  // TRUE TO PRINT PROGRESS

    public static void main(String[] args) throws Exception {
        // --- Read input ---
        File file = new File("input1.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        ArrayList<String> list = new ArrayList<String>();
        String str;

        while((str = br.readLine()) != null) {
            list.add(str);
        }

        // --- Parse input ---
        char[][] map = new char[list.size()][list.get(0).length()]; // [y][x]
        ArrayList<Player> players = new ArrayList<Player>();

        for(int y = 0; y < list.size(); y++) {
            String s = list.get(y);
            for(int x  = 0; x < s.length(); x++) {
                Character ch = s.charAt(x);
                map[y][x] = ch;
                if(ch.equals('E')) {
                    players.add(new Player(0,x,y));
                } else if (ch.equals('G')) {
                    players.add(new Player(1,x,y));
                }
            }
        }

        // Printing
        if(print) {
            System.out.println(players.toString());
            for(int y = 0; y < map.length; y++) {
                for(int x = 0; x < map[y].length; x++) {
                    System.out.print(map[y][x]);
                }
                System.out.println();
            }
            System.out.println();
            TimeUnit.MILLISECONDS .sleep(1000);
            System.out.print("\033[H\033[2J");
        }

        // --- Battle simulation ---
        int turn = 0;
        boolean isElves = true;
        boolean isGoblins = true;

        while(isElves && isGoblins) {
            isElves = false;
            isGoblins = false;
            // Sort player list to get play order.
            Collections.sort(players);

            for(int i = 0; i < players.size(); i++) {
                Player p = players.get(i);

                int direction = shortestPath(p, players, map);
                if(direction == 0) {
                    map[p.y][p.x] = '.';
                    map[p.y-1][p.x] = ((p.race == 0) ? 'E' : 'G');
                    p.y--;
                } else if(direction == 1) {
                    map[p.y][p.x] = '.';
                    map[p.y][p.x-1] = ((p.race == 0) ? 'E' : 'G');
                    p.x--;
                } else if(direction == 2) {
                    map[p.y][p.x] = '.';
                    map[p.y][p.x+1] = ((p.race == 0) ? 'E' : 'G');
                    p.x++;
                } else if(direction == 3) {
                    map[p.y][p.x] = '.';
                    map[p.y+1][p.x] = ((p.race == 0) ? 'E' : 'G');
                    p.y++;
                }
                // If direction = -1. Do nothing

                // Check for adjacent enemies (attack)
                int outcome = attack(p, players, map);
                // -1 - Didn't attack
                // index - Attack and killed someone at index

                if(outcome > 0 && outcome < i) {
                        i--;
                }
            }
            for(Player p : players) {
                if(p.race == 0) {
                    isElves = true;
                } else {
                    isGoblins = true;
                }
            }

            // Printing
            if(print) {
                for(int y = 0; y < map.length; y++) {
                    for(int x = 0; x < map[y].length; x++) {
                        if(map[y][x] == 'G') {
                            System.out.print(ANSI_RED + 'G' + ANSI_RED);
                        } else if(map[y][x] == 'E') {
                            System.out.print(ANSI_GREEN + 'E' + ANSI_GREEN);
                        } else {
                        System.out.print(ANSI_WHITE + map[y][x] + ANSI_WHITE);
                        }
                    }
                    for(Player p : players) {
                        if(p.y == y) {
                            System.out.print(" " + (p.race == 0 ? ANSI_GREEN + 'E' + ANSI_GREEN : ANSI_RED + 'G' + ANSI_RED) + "(" + p.hp + ")");
                        }
                    }

                    System.out.println();
                }
                System.out.println();
                Collections.sort(players);
                TimeUnit.MILLISECONDS .sleep(1000);
                System.out.print("\033[H\033[2J");
            }
            turn++;
        }

        turn--;
        int sumHP = 0;
        for(Player p : players) {
            sumHP += p.hp;
        }
        System.out.println(sumHP + " * " + turn + " = " + (sumHP * turn));

        // Printing again
        if(print) {
            for(int y = 0; y < map.length; y++) {
                for(int x = 0; x < map[y].length; x++) {
                    if(map[y][x] == 'G') {
                        System.out.print(ANSI_RED + 'G' + ANSI_RED);
                    } else if(map[y][x] == 'E') {
                        System.out.print(ANSI_GREEN + 'E' + ANSI_GREEN);
                    } else {
                    System.out.print(ANSI_WHITE + map[y][x] + ANSI_WHITE);
                    }
                }
                for(Player p : players) {
                    if(p.y == y) {
                        System.out.print(" " + (p.race == 0 ? ANSI_GREEN + 'E' + ANSI_GREEN : ANSI_RED + 'G' + ANSI_RED) + "(" + p.hp + ")");
                    }
                }

                System.out.println();
            }
            System.out.println();
        }



    }

    // Calculate the direction a player should go to get to closest players
    // of a different race.
    // Upp = 0, Left = 1, Right = 2, Down = 3
    public static int shortestPath(Player player, ArrayList<Player> players, char[][] map) {
        int minDist = Integer.MAX_VALUE;
        int direction = 3; // Upp 0, Left, 1, Right 2, Down 3

        for(int i = 0; i < players.size(); i++) {

            Player p = players.get(i);

            if(p.race != player.race) {

                // Check if next to player
                if(Math.abs(player.x - p.x) <= 1 && Math.abs(player.y - p.y) <= 1 && p != player
                        && Math.abs(player.x - p.x) + Math.abs(player.y - p.y) == 1) {
                        return -1;
                }

                // Copy map to a new distanceMap
                int[][] distanceMap = new int[map.length][map[0].length];
                for(int y = 0; y < map.length; y++) {
                    for(int x = 0; x < map[y].length; x++) {
                        if(map[y][x] != '.') {
                            distanceMap[y][x] = -2;
                        } else  {
                            distanceMap[y][x] = -1;
                        }
                    }
                }

                int currentDist = 1;
                boolean updatedDist = true;

                while (updatedDist) {
                    updatedDist = false;

                    for(int y = 1; y < distanceMap.length-1; y++) {

                        for(int x = 1; x < distanceMap[y].length-1; x++) {
                            int va = distanceMap[y][x];
                            if(va == currentDist-1 || (p.x == x && p.y == y)) {
                                if(distanceMap[y][x+1] == -1) {
                                    distanceMap[y][x+1] = currentDist;
                                    updatedDist = true;
                                }
                                if(distanceMap[y][x-1] == -1) {
                                    distanceMap[y][x-1] = currentDist;
                                    updatedDist = true;
                                }
                                if(distanceMap[y+1][x] == -1) {
                                    distanceMap[y+1][x] = currentDist;
                                    updatedDist = true;
                                }
                                if(distanceMap[y-1][x] == -1) {
                                    distanceMap[y-1][x] = currentDist;
                                    updatedDist = true;
                                }
                            }
                        }
                    }
                    currentDist++;

                }
                // Update optimal direction to go
                if(distanceMap[player.y+1][player.x] < minDist &&
                    distanceMap[player.y+1][player.x] > 0) {

                    minDist = distanceMap[player.y+1][player.x];
                    direction = 3;
                }

                if(distanceMap[player.y][player.x+1] > 0) {
                    if((distanceMap[player.y][player.x+1] == minDist && direction > 2)
                       || distanceMap[player.y][player.x+1] < minDist) {

                        minDist = distanceMap[player.y][player.x+1];
                        direction = 2;
                    }
                }

                if(distanceMap[player.y][player.x-1] > 0) {
                        if((distanceMap[player.y][player.x-1] == minDist && direction > 1)
                           || distanceMap[player.y][player.x-1] < minDist) {

                            minDist = distanceMap[player.y][player.x-1];
                            direction = 1;
                        }
                }

                if(distanceMap[player.y-1][player.x] <= minDist &&
                    distanceMap[player.y-1][player.x] > 0) {

                    minDist = distanceMap[player.y-1][player.x];
                    direction = 0;
                }

            }
        }

        if(minDist == Integer.MAX_VALUE) return -1;

        return direction;
    }

    public static int attack(Player player, ArrayList<Player> players, char[][] map) {
        Player bestAttackOption = null;
        int minHP = Integer.MAX_VALUE;
        int index = -1;

        for(int i = 0; i < players.size(); i++) {
            Player p = players.get(i);
            if(p.race != player.race) {
                // Check if p is adjacent to the attacking player
                if(Math.abs(player.x - p.x) <= 1 && Math.abs(player.y - p.y) <= 1 && p != player
                        && Math.abs(player.x - p.x) + Math.abs(player.y - p.y) == 1) {
                        if(p.hp < minHP) {
                            bestAttackOption = p;
                            minHP = p.hp;
                            index = i;
                        } else if(p.hp == minHP) {
                            if(bestAttackOption.y > p.y || bestAttackOption.x < p.x) {
                                bestAttackOption = p;
                                minHP = p.hp;
                                index = i;
                            }
                        }
                    }
            }
        }

        if(bestAttackOption != null) {
            //System.out.println("Attacked at x: " + bestAttackOption.x + ", y: " + bestAttackOption.y);
            bestAttackOption.hp -= 3;
            if(bestAttackOption.hp < 0) {
                map[bestAttackOption.y][bestAttackOption.x] = '.';
                players.remove(index);
                return index;
            }
        }
        //System.out.println("Didn't attack");

        return -1;
    }
}
