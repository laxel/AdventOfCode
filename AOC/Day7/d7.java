import java.util.*;
import java.io.*;

public class d7 {
    public static void main(String[] args) throws Exception {
        // Read input
        File file = new File("input.txt");
        BufferedReader br = new BufferedReader(new FileReader(file));

        String str;
        // Map with each letters connections
        HashMap<Character, ArrayList<Character>> connections =
            new HashMap<Character, ArrayList<Character>>();
        // Map that tells how many connections there is TO any letter
        HashMap<Character, Integer> lockedValue = new HashMap<Character, Integer>();

        while ((str = br.readLine()) != null) {
            Character before = str.charAt(5);
            Character after = str.charAt(36);

            // Add connection to connection map
            if(connections.get(before) == null )
                connections.put(before, new ArrayList<Character>());
            if(connections.get(after) == null )
                connections.put(after, new ArrayList<Character>());

            connections.get(before).add(after);

            // Uppdate locked value for connection
            if(lockedValue.get(before) == null)
                lockedValue.put(before, 0);

            if(lockedValue.get(after) == null)
                lockedValue.put(after, 1);
            else
                lockedValue.put(after, lockedValue.get(after) + 1);
        }
        
        System.out.println("/-------------- PART 1 --------------/");
        PriorityQueue<Character> canPopPQ = new PriorityQueue<Character>();
        while(lockedValue.size() > 0) {

            for(Character ch : lockedValue.keySet()) {
                if(lockedValue.get(ch) == 0 && !canPopPQ.contains(ch)) {
                    canPopPQ.add(ch);
                }
            }

            if(canPopPQ.size() <= 0) throw new Exception("Bad input value");

            Character polledLetter = canPopPQ.poll();
            System.out.print(polledLetter);

            for(Character ch : connections.get(polledLetter)) {
                lockedValue.put(ch, lockedValue.get(ch) - 1);
            }
            lockedValue.remove(polledLetter);
        }
        System.out.println();

    }
}
