import java.util.*;
import java.io.*;

public class d7b {
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

        System.out.println("/-------------- PART 2 --------------/");
        StringBuilder sb = new StringBuilder();
        int  availableWorkers = 5;
        // Map that store the time left to "complete" a letter
        HashMap<Character, Integer> letterTimeLeft = new HashMap<Character, Integer>();
        for(Character ch : lockedValue.keySet()) {
            int time = ((int)ch - 64) + 60;
            letterTimeLeft.put(ch, time);
        }
        ArrayList<Character> beingWorkedOn = new ArrayList<Character>();

        PriorityQueue<Character> canPopPQ = new PriorityQueue<Character>();
        int second = 0;
        while(lockedValue.size() > 0) {

            for(int i = 0; i < beingWorkedOn.size(); i++) {
                Character ch = beingWorkedOn.get(i);
                int timeLeft = letterTimeLeft.get(ch) - 1;
                if(timeLeft <= 0) {
                    for(Character child : connections.get(ch)) {
                        lockedValue.put(child, lockedValue.get(child) - 1);
                    }
                    lockedValue.remove(ch);
                    beingWorkedOn.remove(ch);
                    i--;
                    availableWorkers++;
                    sb.append(ch);
                } else {
                    letterTimeLeft.put(ch, timeLeft);
                }
            }

            for(Character ch : lockedValue.keySet()) {
                if(lockedValue.get(ch) == 0 && !canPopPQ.contains(ch) && !beingWorkedOn.contains(ch)) {
                    canPopPQ.add(ch);
                }
            }

            while(canPopPQ.size() > 0 && availableWorkers > 0) {
                Character polledLetter = canPopPQ.poll();
                beingWorkedOn.add(polledLetter);
                availableWorkers--;
            }

            second++;
        }
        System.out.println("Time to complete: " + (second-1));
    }
}
